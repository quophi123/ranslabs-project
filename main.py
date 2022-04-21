from re import A
from warnings import catch_warnings
from pandas.core.indexes.base import Index
import streamlit as st 
import pandas as pd
from EDA import EploratoryDataAnalysis
from Prediction import Makeprediction
from Modelbuilding import Buildmodel
from Visualization import DataVisualization
from FileUpload import UploadFile




Menu = ["Home","About"]
menu = st.sidebar.selectbox('Menu',Menu)










if menu == 'Home':
    operations = ['Select','EDA','Data Visualization','Model Building','Prediction']
    activity=st.sidebar.selectbox('Activity',operations,help='Choose an operation from the menu')

    st.subheader("This is the home area")
    def file():
        data = st.file_uploader('Upload file here',('csv','xlsx'))
        if data is not None:
            df = pd.read_csv(data)
        else:
            df = st.warning('upload data')
        return df
    df = file()





    if activity == 'EDA':
        menu = ['view data','size','shape','show columns','describe','mean','std','null', "count null","corr"]
        #option = st.selectbox('Select EDA to perform',menu,help='select type of eda')
    
        with st.form('eda form'):
            
            option = st.radio('selects',menu)

            st.form_submit_button()
      
        try:
            eda = EploratoryDataAnalysis()
           # with option:
            eda.analyze_data(option,df)
        except:
            st.info('no data uploaded')
        





    elif activity == 'Data Visualization':
        dv = DataVisualization()
        st.write(dv.visualize())









    elif activity == 'Model Building':
        bm = Buildmodel()
        st.write(bm.build())













    elif activity == 'Prediction':
        mp = Makeprediction()
        st.write(mp.predict())


        








else:
    st.subheader("This is the about page")

