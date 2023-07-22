import os
from syori import ai_response
directory = 'content/info'
if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, '.env')
with open(file_path, 'w') as f:
    f.write('CHANNEL_ACCESS_TOKEN =eVtfz1grzEZT9DXQ98IpKyFO5nL/WPGnMGjRKsVrVgLs3hgUtkSVpcPz0MA8Y+XG/aBIVUAJpt/Ys7MnIiZoWsO+dAweFpB0SMH+cjn3AU6eXp/P9cFIfX+46YxequZHV/Y1l7v9zfCJtvidZQBoqAdB04t89/1O/w1cDnyilFU=\n')
    f.write('CHANNEL_SECRET = a7a583f6a83e8898faf4d248278cd774\n')
from linebot.models.responses import RichMenuResponse
import os
from pathlib import Path
import uuid
import openai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
from pyngrok import ngrok
import dotenv
openai.api_key = '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'
def test(question):
    if question=="おはよう":
        response="hallo"
        return response
    else:
        response="まずは挨拶からだよね"
        return response
app = Flask(__name__)
# LineBotApiオブジェクトを作成
dotenv.load_dotenv("content/info/.env")
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)  # リクエストの署名検証を行い、正しければハンドラを実行
    except InvalidSignatureError:
        abort(400)  # 署名が無効な場合はエラーを返す
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text  # 受信したテキストメッセージを取得
    if input_text is not None:
        reply_text=ai_response(input_text)
    else:
        reply_text="error"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)  # 受信したテキストメッセージをそのまま返信
    )
    print("返信",reply_text)
    print("返信完了!!\ntext:", event.message.text)  # 返信が完了したことを表示

ngrok_tunnel = ngrok.connect(5000)  # ポート5000でngrokのトンネルを作成
print('Public URL:', ngrok_tunnel.public_url)  # 公開されたURLを表示

if __name__ == "__main__":
    app.run()  # アプリケーションを実行