# App created by Data Professor http://youtube.com/dataprofessor
# GitHub repo of this app 
# Demo of this app

import streamlit as st
import time

# CSS by andfanilo
# Source: https://discuss.streamlit.io/t/creating-a-nicely-formatted-search-field/1804
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#def remote_css(url):
#    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

#def icon(icon_name):
#    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("App/style.css")
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')


#---------------------------------#
st.write("""# The Pomodoro App
Original app developed by: [Data Professor](http://youtube.com/dataprofessor)
Improvements by: jlmarrugom
""")

# Timer
# Created by adapting from:
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://docs.streamlit.io/en/latest/api.html#lay-out-your-app

button_clicked = st.button("Start")
t1_min = st.number_input("Working time:",min_value=5,max_value=60,value=25,step=5)
t2_min = st.number_input("Rest time:",min_value=0,max_value=30,value=5,step=5)
t1 = t1_min * 60
t2 = t2_min * 60

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 {:2d} minutes is over! Time for a break!".format(t1_min))

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ {:2d} minute break is over!".format(t2_min))
