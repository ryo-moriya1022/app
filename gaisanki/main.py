import streamlit as st
import pandas as pd
from bus_time import main_syori
from bus_time import chenged_pd
from map_dis import URL
from st_time import times
mode_list=["driving","walking","bicycling","transit|walking"]
st.title("シン寝起き時間")
st.write("このシステムは、真に起きればいい時間をバスと時刻表および時間割から導出するシステムとなっています")
st.subheader("講義時間の入力")
st.radio("講義時間",("1限","2限","3限","4限","5限"),key="kougi")
st.subheader("千歳勢or他勢")
st.radio("勢力",("千歳勢","他勢"),key="seiryoku")
if st.session_state["seiryoku"] =="千歳勢":
    seiryoku=0
    st.subheader("移動方法")
    mode=st.radio("移動方法",(mode_list))
else:
    seiryoku=1
    mode=mode_list[3]
st.subheader("家の場所")
st.text_input("家の場所",key="start")
st.subheader("本気を出したとき起床から準備までにかかる時間(%H:%M)")
st.text_input("時間(例:10分の場合は10と入力する 1時間10分の場合は1:10)",key="times")
nearest_bus = st.button("計算開始")
if nearest_bus:
    if not st.session_state["start"]:
        st.error("家の場所が正しく入力されていません")
    if not st.session_state["times"]:
        st.error("時間が入力されていません")
    else:
        st.subheader("計算結果")
        result = main_syori(st.session_state["kougi"], seiryoku)
        trans_time,urls=URL(st.session_state["start"],seiryoku,mode)
        result_time=times(result,trans_time,str(st.session_state["times"]))
        time_data=chenged_pd(result_time,trans_time,st.session_state["times"],mode)
        st.write("計算結果")
        st.write(time_data)
        st.write(urls)
        st.write("バス時間")
        st.write(result)