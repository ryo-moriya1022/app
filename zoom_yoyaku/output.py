import streamlit as st
from zoom_enter import data_zoom
st.set_page_config(
    page_title="URL自動実行システム",
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com"
    }
)
st.title("URL自動実行システム")
st.header("概要")
st.write("このプログラムは1週間以内の任意の時間に任意のURLを作動させるシステムとなっています")

st.header("URLの入力  曜日、時間の入力")
urls=st.text_input("URL") 
youbi=st.selectbox("曜日",("日曜日","月曜日","火曜日","水曜日","木曜日","金曜日","土曜日"))
times=st.text_input("時間の入力 例)日曜日午前9時に予約したい場合 '09:00'と入力")
st.write("")
st.header("予約")
st.write("ボタンを押すことで予約ができます。現在目的の時間が過ぎた後に予約すると、処理が発生しているバグあり注意")
st.write("")
if st.button("予約",key="data"):
    data_zoom(urls,youbi,times)
st.write("")
st.write("予約の取り消しをします")
if st.button("取消",key="tor"):
    st.stop()