
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()


st.markdown("""<h1> Home Area </h1>""", unsafe_allow_html=True)


#  st.sidebar.selectbox('Choose an option',('main','home','school'))


def load_lottiefiles(filepath: str):
    with open(filepath, 'r') as file:
        return json.load(file)

#def load_lottievideo(url: str):
    #r = requests.get(url)
    #if r.status_code != 200:
        #return  None
    #return r.json()

lottie = load_lottiefiles("assets/dataanalytics.json")
lottie1 = load_lottiefiles("assets/data1.json")
lottie2 = load_lottiefiles("assets/data2.json")
#lottie_video = load_lottievideo("https://iconscout.com/lottie/data-analytics-information-presentation-3914375")



#st_lottie(lottie_video(), key='helo')


#st.video("assets/da.mp4")


col1,col2,col3 = st.columns(3)
with col1:
    st_lottie(
    lottie,
    speed=0.5,
    height=300,
    loop=False,
    quality='high',
    
    )

with col2:
    st_lottie(
    lottie2,
    speed=0.5,
    height=300,
    loop=False,
    quality='high',
    
    )
with col3:
    st_lottie(
    lottie1,
    height=300,
    loop=True,
    quality='high',
    
    )
