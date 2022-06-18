from pandas import options
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#from pages import FileUpload 


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




# uploading your dataset
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
try:
    menu = ['view data','size','shape','show columns','describe','mean','std','null', "count null","corr"]
    option = st.selectbox('Select EDA to perform',menu,help='select type of eda')

    if  option == 'view data':
        view_type = st.selectbox('select view type',('by rows','by columns'))
        if view_type == 'by rows':
            view_option = st.radio('select view type',('head','tail','preferred number'))
            if view_option == 'head':
                st.dataframe(data.head())
            elif view_option == 'tail':
                st.dataframe(data.tail())
            else:
                number = st.slider('slide to your preferred number',min_value=1,max_value=data.shape[0])
                st.dataframe(data.head(number))
        else:
            column_view = st.multiselect('showing data by columns',data.columns)
            st.dataframe(data[column_view])

    elif option == 'size':
        st.write(data.size)

    elif option == 'show columns':
        st.dataframe(data.columns )

    elif option == 'describe':
       st.dataframe(data.describe())

    elif option == 'shape':
        st.write('dataset has `{}` columns and `{}` rows'.format(data.shape[0],data.shape[1]))

    elif option == 'mean':
        # calculating for mean of the dataset
        st.dataframe(data.mean())
    elif option == 'std':
        #claculating the standard deviation
        st.dataframe(data.std())
    elif option == 'null':
        st.write(data.isnull())

    elif option =='count null':
        st.dataframe(data.isnull().sum())

    elif option =='corr':
        # checking for correlation between columns of the data set

        col1 = st.sidebar.selectbox('select first column',data.columns)
        col2 = st.sidebar.selectbox('select second column',data.columns)
        a = data[f"{col1}"]
        b = data[f'{col2}']
        st.write(a.corr(b))
    else:
        st.write(option)
except:
    st.error("No Data Uploaded")
