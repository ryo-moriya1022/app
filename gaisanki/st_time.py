import pandas as pd
import streamlit as st
import datetime as dt

def convert_to_datetime(time_str):
        parts = time_str.split()
        if parts[1] == "hours":
            hour = int(parts[0])
            minute = int(parts[2])
        elif parts[1] == "mins":
            hour = 0
            minute = int(parts[0])
        else:
            raise ValueError("Invalid time format")
        time_delta = dt.timedelta(hours=hour, minutes=minute)
        return time_delta
def chenge_datetime(set_time):
    if ":" in set_time:
        try:
            set_time = dt.datetime.strptime(set_time, "%H:%M")
            # 現在の日付に設定時刻の日付を合わせる
            set_time = set_time.replace(year=dt.datetime.today().year, month=dt.datetime.today().month, day=dt.datetime.today().day)
            return set_time
        except ValueError:
            print("時刻の変換に失敗しました。正しい形式で入力してください。")
            return None
    else:
        set_time = dt.timedelta(hours=0, minutes=int(set_time))
        return dt.datetime.combine(dt.datetime.today(), dt.time()) + set_time

def time_keisan(bus_time, time_delta, set_time):
    result_time = bus_time - time_delta - set_time
    return result_time

def times(time_df, trans_time, set_time):
    time_format = '%H:%M'
    bus_time_str = time_df.iloc[0, 0]
    
    if bus_time_str == "-":
        bus_time_str = time_df.iloc[0, 1]
    
    bus_time = dt.datetime.strptime(bus_time_str, time_format)
    
    # 現在の日付にバスの出発時刻を合わせる
    bus_time = bus_time.replace(year=dt.datetime.today().year, month=dt.datetime.today().month, day=dt.datetime.today().day)
    
    print("バス出発時刻:", bus_time)
    
    time_delta = convert_to_datetime(trans_time)
    print("変換された時間差:", time_delta)
    
    set_time = chenge_datetime(set_time)
    print("変換された設定時刻:", set_time)
    
    result_time = time_keisan(bus_time, time_delta, set_time)
    return result_time

# テスト用のデータ
data = {
    'chitose': ['8:36', '-', '8:51', '8:54'],
    'minami_chitose': ['must_time', '8:36', '8:51', '8:54'],
    'kenkyuto': ['8:36', '8:36', '8:51', '8:54'],
    'honbuto': ['8:36', '8:36', '8:51', '8:54']
}

data = pd.DataFrame(data)
result = times(data, "11 hours 32 mins", "10")
print("計算結果:", result)
