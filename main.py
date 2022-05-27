from re import A
from warnings import catch_warnings
from pandas.core.indexes.base import Index
import streamlit as st 
import pandas as pd
#from EDA import analyze_data
#from Prediction import Makeprediction
#from Modelbuilding import app
#from Visualization import DataVisualization
#from FileUpload import file_upload

import page2,page1,Modelbuilding,EDA,Prediction,FileUpload


Menu = ["Home","About"]
menu = st.sidebar.selectbox('Menu',Menu)


PAGES = {
    "UploadFile":FileUpload,
    "EDA":EDA,
    "Modelbuilding":Modelbuilding,
    "Prediction":Prediction
}








if menu == 'Home':
    st.subheader("This is the home area")
    st.sidebar.title('Activities')
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    #file_upload()

else:
    st.subheader("This is the about page")

