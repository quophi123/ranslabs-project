import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#site configurations 
logo = Image.open('logo.jpg')
st.set_page_config(page_title='ml automate', page_icon=logo)

hid_menu_style = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            </style>
"""
st.markdown(hid_menu_style,unsafe_allow_html=True)



def app():
    chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
    st.area_chart(chart_data)


    
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)



app()