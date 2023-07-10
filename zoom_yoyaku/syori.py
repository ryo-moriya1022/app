import datetime as dt
import streamlit as st
from time import sleep
import webbrowser
import streamlit as st 
def webopen(urls):
    webbrowser.open(urls)
def times(input_dt :dt.datetime,urls):
    now_dt=dt.datetime.now()+dt.timedelta(hours=9)
    if input_dt < now_dt:
        st.stop()
    else:
        while True:
            now_dt = dt.datetime.now()+dt.timedelta(hours=9)
            if abs((now_dt - input_dt).total_seconds()) < 1:
                st.write("zikko")
                webopen(urls)
                break
            sleep(1)