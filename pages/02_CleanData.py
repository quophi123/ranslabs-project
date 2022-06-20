from dataclasses import replace
from click import option
from requests import head
import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
from traitlets import default

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




data = file()




st.subheader("Clean Your Data Here")


activities = ['Null','Change DataTypes']
option = st.selectbox("Select Activity Type",activities)
if option == "Null":
    st.header('Work on your null values')
    menu = st.selectbox("Type",("Drop Null","Replace Null"))
    if menu == "Drop Null":
        axis = st.selectbox("Select Axis to drop",("","By Column","By Rows"),)
        if axis == "By Column":
            columns_to_drop = st.selectbox("Select columns to drop from the dataset",data.columns)
            if st.button('Confirm drop'):
                new = data.drop(columns_to_drop,inplace=True, axis=1)
                st.dataframe(new)


        elif axis == "By Rows":
            if st.button('Confirm Remove row'):
                n = data.dropna(axis=0)
                st.dataframe(n)


    elif menu == "Replace Null":
        replace_type = st.radio("Select replace type",('By Mean','By Zero','Custume Repalce'))

        if replace_type == 'By Mean':
            columns = st.multiselect("Select columns to raplce values in",data.select_dtypes(include=['float']).columns)
            mean = data[columns].mean()
            st.write(mean)
            st.write(data[columns].fillna(value=mean, inplace=True))
            st.write(data)


        elif replace_type == 'By Zero':
            columns = st.selectbox("Select column to raplce values in",data.select_dtypes(include=['float']).columns)
            value = int(0)
            st.write(data[columns].fillna(value=value, inplace=True))
            st.dataframe(data)
        

        elif replace_type == 'Custume Repalce':
            value = float(st.number_input("Enter your prefered replacable value",))
            columns = st.selectbox("Select columns to raplce values in",data.select_dtypes(include=['float']).columns)
            data=data[f'{columns}'].fillna(value=value, inplace=True)
            st.dataframe(data)






elif option == "Change DataTypes":
    st.header('Change your data types here')