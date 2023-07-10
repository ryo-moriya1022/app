import datetime as dt
import streamlit as st
from time import sleep
import webbrowser
import streamlit as st 
def times(input_dt :dt.datetime,urls):
    now_dt=dt.datetime.now()+dt.timedelta(hours=9)
    if input_dt < now_dt:
        st.stop()
    else:
        while True:
            now_dt = dt.datetime.now()+dt.timedelta(hours=9)
            if abs((now_dt - input_dt).total_seconds()) < 1:
                st.write(urls)
                webbrowser.open(urls,new=1,autoraise=True)
                break
            sleep(1)