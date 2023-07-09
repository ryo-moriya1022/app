import datetime
import streamlit as st
from time import sleep
import webbrowser
import streamlit as st 
def webopen(urls):
    webbrowser.open(urls)
def times(dt :datetime.datetime,urls):
    now_dt = datetime.datetime.now().replace(second=0)
    if dt < now_dt:
        st.stop()
    else:
        while True:
            now_dt = datetime.datetime.now().replace(second=0)
            if abs((now_dt - dt).total_seconds()) < 1:
                webopen(urls)
                break
            sleep(1)