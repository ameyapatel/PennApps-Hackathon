
from cProfile import run
import streamlit as st
st.title("NAME")
import datetime

def set_alarm():
    priority = st.text_input("Priority: High, medium, or low")
    if st.button("Set Alarm"):
        priority = st.text_input("Priority: High, medium, or low")
        while(priority != "High", priority != "Medium", priority != "Low"):
            priority = st.text_input("Priority: High, medium, or low")
        time_off = st.text_input("Alarm time:")

def main():
    set_alarm()


def randomize_sounds():

#def waking_up():

#def profile():

#def adding_friends():

#def notifs():
    time_off = st.text_input("Alarm time:")
    if st.button("Save"):
        st.info("Alarm going off at: " + time_off)

        while True:
            if datetime.datetime.now().strftime("%H:%M:%S") == time_off:
                break

        st.write("Alarm going off")

