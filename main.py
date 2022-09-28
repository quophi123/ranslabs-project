import streamlit as st
import numpy as np
import matplotlib as plt
import pandas as pd
import plotly_express as px
import streamlit_theme as stt
import json
from PIL import Image
import seaborn as sns
from streamlit.components.v1 import html
from streamlit_lottie import st_lottie
from Components.Navbar import Navbar;
from Components.Config import Config;

Config()

Navbar()

# st.markdown("""<h1> Welcome to Ml Automate </h1>""", unsafe_allow_html=True)
st.header("Welcome to `Ml Automate`")

def load_lottiefiles(filepath: str):
    with open(filepath, 'r') as file:
        return json.load(file)



lottie = load_lottiefiles("assets/ai.json")
lottie1 = load_lottiefiles("assets/data1.json")
lottie2 = load_lottiefiles("assets/programming-computer.json")


st.markdown(
    "<h5>Ml Automate Process</h5>",unsafe_allow_html=True
)
img = Image.open('assets/ml.png')
st.image(img)


col1, col2, col3 = st.columns([2,2,2])

with col2:
    st.markdown(
    "<h5>Machine learning and data science made easy</h5>",unsafe_allow_html=True
    )
    st.markdown("""
    From data preparation through value tracking, `Ml Automate` 
    equips you with enterprise-grade stability 
    and scalability you can count on.It makes it easy to ***analyze data,scales 
    your data,build `ml` models*** and ***make prediction*** very easy for 
    machine learning engineers and data scientists.:sunglasses:
    """)



    




with col3:
    st_lottie(
        lottie2,
        speed=1,
        height=300,
        width=300,
        loop=True,
        quality='high',

    )


tab1,tab2,tab3 = st.columns(3)


# st.write(data)
with tab1:
    size = st.slider('slide', min_value=100, max_value=1000)
    data = np.random.random_sample(size=size)
    data1 = np.random.random_sample(size=size)
    data2 = np.random.random_sample(size=size)


with tab2:
    st_lottie(
        lottie1,
        speed=1,
        height=300,
        loop=True,
        quality='high',
        key='hello'


    )


with tab3:
    size = st.slider('sliders', min_value=100, max_value=1000)
    
    data = np.random.random_sample(size=size)

    data1 = data * 2
    st.area_chart(data)
