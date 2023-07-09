import streamlit as st
import datetime  as dt
#chenge str to datetime
def chenge_to_dt(input_time, now_year, now_month, now_day):
    dt_input_time=(
        str(now_year)+"-"
        +str(now_month)+"-"
        +str(now_day)+'-'
        +input_time
    )
    dt_input_time=dt.datetime.strptime(
        dt_input_time,"%Y-%m-%d-%H:%M"
        )
    dt_input_time=dt_input_time+dt.timedelta(hours=9)
    return dt_input_time
# now time get 
now_time=dt.datetime.now()
# chenge now time to timezone(japan)
now_time_datezone=now_time+dt.timedelta(hours=9)
# concat input time to year and day and month
now_year=now_time.year
now_month=now_time.month
now_day=now_time.day
urls=st.text_input('URL',key='urls')
st.date_input(
    "date",
    min_value=now_time_datezone,
    max_value=now_time_datezone+dt.timedelta(days=14),
    value=now_time_datezone
)
st.text_input(
    "input_date",
    value="09:00",
    key='times'
)
dt_input_time=chenge_to_dt(
    st.session_state["times"],
    now_year,now_month,now_day
    )
st.write(now_time_datezone,dt_input_time)