import streamlit as st
import webbrowser as we
def web():
    we.open("https://www.netflix.com/jp/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")
st.title("test")
st.button('予約',on_click=web)

