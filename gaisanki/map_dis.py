import requests
import streamlit as st
def get_travel_duration(api_key, origin, destination,mode):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    
    params = {
        "key": api_key,
        "origins": origin,
        "destinations": destination,
        "mode":mode, 
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["status"] == "OK":
            element = data["rows"][0]["elements"][0]
            if "duration" in element and "text" in element["duration"]:
                duration=element["duration"]["text"]
                return duration
            else:
                st.error("家の場所の入力が正しくありません")
        else:
            return "Error fetching data"
    except requests.exceptions.RequestException:
        st.error("wifiに接続してません")
def URL_output(start,mode,seiryoku):
    if seiryoku ==1:
        if mode=="transit|walking":
            mode="transit"
        print(seiryoku)
        urls=f"https://www.google.com/maps/search/{start}から南千歳駅前タクシー乗り場まで{mode}"
    if seiryoku ==0:
        urls=f"https://www.google.com/maps/search/{start}から北海道千歳市末広６丁目４−４まで{mode}"
    return urls
def URL(start,seiryoku,mode):
    print("win")
    api_key = "AIzaSyCz41p1cuYCkXsqZz2uPCJXi2JffE_ETho"
    if seiryoku==0:
        origin = start
        destination = "42.828757, 141.652515"
        duration = get_travel_duration(api_key, origin, destination,mode)
        urls=URL_output(start,mode,seiryoku)
        return duration,urls
    if seiryoku==1:
        origin=start
        destination="42.808914, 141.675946"
        duration=get_travel_duration(api_key,origin,destination,mode)
        urls=URL_output(start,mode,seiryoku)
        return duration,urls
