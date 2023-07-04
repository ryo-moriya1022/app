import webbrowser
from time import sleep
import streamlit as st
def zoom_ki(urls):
    webbrowser.open(urls)
    sleep(5)
    st.stop()