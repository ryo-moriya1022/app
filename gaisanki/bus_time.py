# ライブラリ設定
import string
import fitz
import re
import pandas as pd
import numpy as np
import streamlit as st
# PDFを読み込む
def kougizian(kougi):
    if kougi=="1限":
        start=900
    if kougi=="2限":
        start=1045
    if kougi=="3限":
        start=1315
    if kougi=="4限":
        start=1500
    if kougi=="5限":
        start=1645
    return start

def PDF_inport():
    time_list = []
    i=0
    def remove_japanese_lines(text):
        pattern = re.compile(r'[^\x01-\x7E]+')  # ASCII文字以外を含む行をマッチさせる正規表現パターン
        lines = text.splitlines()
        cleaned_lines = [line for line in lines if not pattern.search(line)]
        return '\n'.join(cleaned_lines)

    def remove_english_lines(text):
        # 行に英字が含まれない場合のみ抽出
        filtered_lines = [line for line in text.split('\n') if not any(char in string.ascii_letters for char in line)]
        # テキストを改行で連結して返す
        return '\n'.join(filtered_lines)

    def chenge_pandas(time_list):
        column_list=["chitose","minami_chitose","kenkyuto","honbuto"]
        time_table=pd.DataFrame(data=time_list,columns=column_list)
        return time_table

    def chitose_minami_chitose_split(time_table):
        chitose_pd = time_table[time_table['chitose'] != '-']
        minami_chitose_pd = time_table[time_table['minami_chitose'] != '-']
        return chitose_pd,minami_chitose_pd

    def data_split_point(lines):
        i=0
        count=0
        while True:
            if lines[i]=='-':
                count+=1
                if count==2:
                    return i
            i=i+1
    filename = "bustime3.pdf"
    doc = fitz.open(filename)
    page = doc.load_page(0)
    text = page.get_text()
    #cl_text = text
    cl_text=remove_japanese_lines(text)
    cl_text=remove_english_lines(cl_text)
    lines=cl_text.split('\n')   
    split_point=data_split_point(lines)
    while not (lines[i]==lines[i+1] and int(lines[i+2].replace(":",""))>1800):
        first_line=lines[i:i+4]
        time_list.append(first_line)
        i=i+split_point
    doc.close()

    time_table=chenge_pandas(time_list)
    chitose_pd,minami_chitose_pd=chitose_minami_chitose_split(time_table)
    return chitose_pd,minami_chitose_pd

def must_bus_time(start_time,time_pd:pd.DataFrame):
    time_list=[]
    number=[x for x in range(len(time_pd.index))]
    for time in time_pd.iloc[:, 3]:
        time=time.replace(":","")
        time_list.append(time)
    time_dict=dict(zip(time_list,number))
    filtered_times = [int(time) for time in time_list if int(time) < start_time]
    nearest_time = min(filtered_times, key=lambda x: abs(x - start_time))
    nearest_time=f"{nearest_time:04d}"
    nearest_time=f"{nearest_time[:2]}:{nearest_time[2:]}"
    if nearest_time.startswith("0"):
        nearest_time=nearest_time[1:]
    time_table=time_pd.loc[time_pd["honbuto"]==nearest_time]
    time_table.rename(index={time_table.index[0]: "must_time"}, inplace=True)
    return time_table

def main_syori(kougi_time,seiryoku):
    chitose_pd,minami_chitose_pd=PDF_inport()
    start_time=kougizian(kougi_time)
    if seiryoku==0:
        time_pd=chitose_pd
    else:
        time_pd=minami_chitose_pd
    time_table=must_bus_time(start_time,time_pd)
    return time_table

def chenged_pd(result_time,trans_time,mazi_time,mode):
    def make_clickable(val):
        return '<a href="{}">{}</a>'.format(val,val)
    time_data={
        "準備にかかる時間":[str(mazi_time)],        
        "家からの所要時間":[str(trans_time)],
        "起きる時間":[str(result_time)],
        "移動方法"  :[mode]
        }
    time_data=pd.DataFrame(time_data)
    time_data.style.format(make_clickable)
    return time_data
