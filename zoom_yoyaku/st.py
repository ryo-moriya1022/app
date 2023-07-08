import streamlit as st
import datetime as dt
from input import times
st.set_page_config(
    page_title="URL自動実行システム",
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com"
    }
)
def check(date_dt:dt.datetime,time_dt:dt.datetime):
    try:
        datetime_combined = dt.datetime.combine(date_dt, time_dt)
        st.write("入力された時刻は",datetime_combined)
        if datetime_combined<dt.datetime.today():
            st.error("過去の予約はできません")
        return datetime_combined
    except TypeError:
        pass
st.write("")
st.title("URL自動実行システム")
st.header("概要")
st.write("このプログラムは1週間以内の任意の時間に任意のURLを作動させるシステムとなっています")
st.header("URLの入力 曜日 時間の入力")
urls=st.text_input("URL",key="urls")
st.date_input(
    'Input date',
    min_value=dt.datetime.now(),
    max_value=dt.datetime.now()+dt.timedelta(days=14),
    value=dt.datetime.now(),
    key="date"
)
st.text_input(
    'times',
    value=
    str(dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).hour)+":"+str(dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).minute),
    key="times"
)
time_str = st.session_state["times"]
time_dt = dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))
try:
    time_dt=dt.datetime.strptime(time_str, "%H:%M").time()
except ValueError:
    st.error("入力にエラーがあります。正しい形式は%H:%Mです")
date_dt = st.session_state["date"]
datetime_combined=check(date_dt,time_dt)
st.header("予約")
st.write("ボタンを押すことで予約ができます。")
st.button('予約',on_click=times,args=(datetime_combined,
    st.session_state["urls"])
    )
st.write("予約の取り消しをします")
if st.button("取消",key="tor"):
    st.stop()