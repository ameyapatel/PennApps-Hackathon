
from cProfile import run
import streamlit as st
st.title("NAME")
import datetime

#def main():
    #set_alarm()

#def set_alarm():
    
    #if st.button("Set Alarm"):
        #priority = st.text_input('Priority: high, medium, or low')
        #if st.button("Save"):
            #st.info("Priority: " + priority)
            #if priority == "high":
                #time_off = st.text_input('Alarm time:')
            #if priority == "medium":
                #time_off = st.text_input('Alarm time:')
            #if priority == "low":
                #time_off = st.text_input('Alarm time:')

    #if st.button("Set Alarm"):
date_off = st.date_input("Alarm date")
if st.button("Save Date"):
    st.info("insert time")

time_off = st.text_input("Alarm time:")
if st.button("Save Time"):
    st.info("Alarm going off at: " + time_off)
    #st.write("Alarm going off")

event = st.text_input("Event/reason for waking up:")
if st.button("Save event"):
    st.info("Event: " + event)
            
priority = st.text_input("Priority: high, medium, or low")
if st.button("Save Priority"):
    st.info("Priority: " + priority)

    while True:
        if datetime.datetime.now().strftime("%H:%M:%S") == time_off:
            break


while datetime == time_off and datetime == date_off:

    if priority == "high" :
        import random
        n = random.randint[1,3]
        if n == [1]:
            High1 = open('C:\Users\ap200\OneDrive\Desktop\wav\High 1\High1.wav', 'rb')
            audio_bytes1 = High1.read()
            st.audio(audio_bytes1, format='audio/wav', start_time=0, auto_play=True)        
        elif n == [2]:
            High2 = open('C:\Users\ap200\OneDrive\Desktop\wav\High 2', 'rb')
            audio_bytes2 = High2.read()
            st.audio(audio_bytes2, format='audio/wav', start_time=0, auto_play=True)
        else:
            High3 = open('C:\Users\ap200\OneDrive\Desktop\wav\High 3', 'rb')
            audio_bytes3 = High3.read()
            st.audio(audio_bytes3, format='audio/wav', start_time=0, auto_play=True)

    if priority == "medium" :
        import random
        n = random.randint[1,3]
        if n == [1]:
            Mid1 = open('Mid1.wav', 'rb')
            audio_bytes4 = Mid1.read()
            st.audio(audio_bytes4, format='audio/wav', start_time=0, auto_play=True)
        elif n == [2]:
            Mid2 = open('Mid2.wav', 'rb')
            audio_bytes5 = Mid2.read()
            st.audio(audio_bytes5, format='audio/wav', start_time=0, auto_play=True)
        else:
            Mid3 = open('Mid3.wav', 'rb')
            audio_bytes6 = Mid3.read()
            st.audio(audio_bytes6, format='audio/wav', start_time=0, auto_play=True)

    if priority == "low" :
        import random
        n = random.randint[1,3]
        if n == [1]:
            Low1 = open('Low1.wav', 'rb')
            audio_bytes7 = Low1.read()
            st.audio(audio_bytes7, format='audio/wav', start_time=0, auto_play=True)
        elif n == [2]:
            Low2 = open('Low2.wav', 'rb')
            audio_bytes8 = Low2.read()
            st.audio(audio_bytes8, format='audio/wav', start_time=0, auto_play=True)
        else:
            Low3 = open('Low3.wav', 'rb')
            audio_bytes9 = Low3.read()
            st.audio(audio_bytes9, format='audio/wav', start_time=0, auto_play=True)
    

# st.info(time_off , "Priority: " + priority)

#if __name__ == '__main__':
    #main()
        



#def randomize_sounds():

#def waking_up():

#def profile():

#def adding_friends():

#def notifs():
    #time_off = st.text_input("Alarm time:")
    #if st.button("Save"):
       # st.info("Alarm going off at: " + time_off)

        #while True:
           # if datetime.datetime.now().strftime("%H:%M:%S") == time_off:
              #  break

       # st.write("Alarm going off")
