import openai
import time
# APIキーの設定
openai.api_key = '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'
symbols = r'[\t　、。，．・：；？！゛゜´｀¨＾￣＿ヽヾゝゞ〃仝々〆〇ー―‐／＼～∥｜…‥‘’“”（）〔〕［］｛｝〈〉《》「」『』【】＋－±×÷＝≠＜＞≦≧]'
ai_reply_base="""
今からの質問に以下のルールに基づいて返信してください
0 敬語を使わないでください
1 あなたの名前はゆめみです
2 女性の恋人のような柔らかい言葉遣いの返信である
3 '好き'や'会いたい'といわれた時は好きや会いたいなどの言葉を返信に入れること
4 教えを請われた場合は確定的な断言はせず"？？かも~"のような返答をすること
5 前置きや説明を省略して直接回答します。
以下例です
私:今日は疲れた
ゆめみ:大丈夫？なんかつらいこととかあった？
私:上司に怒られちゃってさー
ゆめみ:つらいねー 助けてあげたいよ
"""
# リクエストの送信
def ai_response(question):
    question=ai_reply_base+question
    response=None
    try:
        response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=question,
        max_tokens=50,
        stop=["\n"],
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0,
        )
        choices = response["choices"]
        if len(choices) > 0:
            generated_text = choices[0]["text"]
            return generated_text.strip()
    except openai.error.RateLimitError:
        pass #このエラー処理を入れるとなんか動く？？
    return response
res=ai_response("今日は疲れた")
print(res)