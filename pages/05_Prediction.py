import streamlit as st 
from PIL import Image
import pandas as pd
import numpy as np
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


st.subheader("Make Predictions Here")

def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    else:
        df = st.warning("Upload Data")
    return df




data = file()







#number_of_columns = int(st.number_input("Please enter the number for columns"))

c = data.columns

enteries = list()
for i in c:
    column = st.text_input(f" {i}")
    enteries.append(column)

st.write(np.array(enteries).reshape(1,-1))