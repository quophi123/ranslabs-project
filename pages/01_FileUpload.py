import streamlit as st
import pandas as pd
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




  
def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    else:
        df = st.warning("Upload Data")
    return df
        
data1= file()