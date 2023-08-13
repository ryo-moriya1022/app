import streamlit as st
import datetime  as dt
from input import times
def main():
    st.set_page_config(
        page_title="URL自動実行システム",
        layout="wide", 
        initial_sidebar_state="auto", 
        menu_items={
            'Get Help': 'https://www.google.com',
            'Report a bug': "https://www.google.com"
        }
    )
    #chenge str to datetime
    def chenge_to_dt(input_time, now_days):
        dt_input_time=(
            now_days+"-"+input_time
        )
        dt_input_time=dt.datetime.strptime(
            dt_input_time,"%Y-%m-%d-%H:%M"
            )
        return dt_input_time

    def errors(dt_input_time,now_time_datezone):
        if dt_input_time<=now_time_datezone:
            st.error("過去の予約はできません")
    # now time get 
    now_time=dt.datetime.now()
    # chenge now time to timezone(japan)
    now_time_datezone=now_time

    st.title("URL自動実行システム")
    st.header("概要")
    st.write("このプログラムは1週間以内の任意の時間に任意のURLを作動させるシステムとなっています")
    st.header("URLの入力 曜日 時間の入力")
    urls=st.text_input('URL',key='urls')
    st.date_input(
        "date",
        min_value=now_time_datezone,
        max_value=now_time_datezone+dt.timedelta(days=14),
        value=now_time_datezone,
        key="date"
    )
    st.text_input(
        "input_date",
        value="09:00",
        key='times'
    )
    dt_input_time=chenge_to_dt(
        st.session_state["times"],
        str(st.session_state["date"]),
        )
    errors(dt_input_time,now_time_datezone)
    st.write(now_time_datezone,dt_input_time)
    st.header("予約")
    st.write("ボタンを押すことで予約ができます。")
    st.button('予約',on_click=times,args=(
        dt_input_time,
        st.session_state["urls"],
        )
        )
    st.write("予約の取り消しをします")
    if st.button("取消",key="tor"):
        st.stop()
if __name__=="__main__":
    main()