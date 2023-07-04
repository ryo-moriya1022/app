import schedule as sc
from time import sleep
import streamlit as st
from zoom_kido import zoom_ki
def data_zoom(urls,youbi,time):
    if youbi=="日曜日":
        sc.every().sunday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="月曜日":
        sc.every().monday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="火曜日":
        sc.every().tuesday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="水曜日":
        sc.every().wednesday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="木曜日":
        sc.every().thursday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="金曜日":
        sc.every().friday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)
    if youbi=="土曜日":
        sc.every().saturday.at(time).do(zoom_ki,urls)
        while True:
            sc.run_pending()
            sleep(59)