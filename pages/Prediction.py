#importing packages
import streamlit as st
import pandas as pd
import numpy as np

#import app components
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()

st.markdown("""<h1> Prediction  Area </h1>""", unsafe_allow_html=True)


def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    return df












#number_of_columns = int(st.number_input("Please enter the number for columns"))
try:
    data = file()
    c = data.columns

    enteries = list()
    for i in c:
        column = st.text_input(f" {i}")
        enteries.append(column)

    st.write(np.array(enteries).reshape(1,-1))
except:
    st.warning('Upload Data')