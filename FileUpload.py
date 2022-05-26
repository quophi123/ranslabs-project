import streamlit as st
import pandas as pd



  
def app():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    if data is not None:
        df = pd.read_csv(data)
    else:
        df = st.warning("Upload Data")
    return df
        