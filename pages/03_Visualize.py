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

visuals = ['Pie Chart','Bar Chart','Line Chart','Heat Map']

plot = st.radio('Select Graph Type',visuals,horizontal=True)


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
if plot == "Pie Chart":
    st.subheader('Showing graph for pie chart')
    columns = st.multiselect("Select columns to plot",data.columns.astype(float))
    if st.button(f'Generate {plot}'):
        st.plotly_chart(data=data)
        st.write("plots")
        



elif plot == "Bar Chart":
    st.subheader('Showing graph for bar chart')
    columns = st.multiselect("Select columns to plot",data.columns)
    if st.button(f'Generate {plot}'):
        st.write(data[columns])
        graph = st.bar_chart(data=data[columns])
        st.write("plots")



elif plot == "Line Chart":
    st.subheader('Showing graph for line chart')
    columns = st.multiselect("Select columns to plot",data.columns)
    if st.button(f'Generate {plot}'):
        st.line_chart(data=data[columns])
        st.write("plots")
        



elif plot == "Heat Map":
    st.subheader('Showing graph for heat map')
    if st.button(f'Generate {plot}'):
        st.graphviz_chart()
        st.write("plots")
        
    
