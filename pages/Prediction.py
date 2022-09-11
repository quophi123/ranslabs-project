#importing packages
import io
import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk
import os
import sys
import time

#import app components
from Components.Navbar import Navbar;
from Components.Config import Config;
from pathlib import Path




Config()

Navbar()

st.markdown("""<h1> Prediction  Area </h1>""", unsafe_allow_html=True)



def uploadModel(filename):
        # load the model from disk
        loaded_model = pk.load(open(filename, 'rb'))
        return loaded_model





file_source = st.selectbox('Choose a file source',('local','Onsite'))
if file_source == 'local':
    file = st.file_uploader("Upload a file", type="sav")
    names = (dir(file))
    #st.write(names)
    for name in names:
        if name == 'name':
            filename = file.name
    try:
        filename = filename
        @st.cache(suppress_st_warning=True,show_spinner=False,)
        def getFilePath(filename):
            for root , dirs, files in os.walk(Path.home()):
                for name in files:
                    if name== filename:
                        filename = os.path.abspath(os.path.join(root, name))
            return filename
        with st.spinner(text='Wait while we generate your chart....'):
            time.sleep(1)
            filename = getFilePath(filename=filename)
        st.success('Done')
        
                    
        
        columns = st.text_input('Enter the columns name seperated by comma')
        column_names = columns.split(',')
        #creating a list of column names that   will be used in the output  filename
        enteries = []
        with st.expander('Enter your values'):
            for name in column_names:
                column = st.number_input("Enter the value for {}".format(name))
                enteries.append(column)
    except:
        st.write('No file uploaded')
        st.stop()
    
        
        
else:
    available_models = []
    g = os.getcwd()
    for i in os.listdir(g):
        if i.endswith('.sav'):
            available_models.append(i)
            
        



    with st.expander("Select Your Model From The available models"):
        v = st.selectbox('Select your model',available_models)




    directory= os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s="\\"
    else:
        s="/"
    filename = v

    try:
        name = filename.split('.')
        name.pop(0)
    except:
        st.stop()



    try:
        variables = []
        count = 0
        for i in name:
            variables.append(i)
            count += 1
            if count >= len(name)-1:
                break
        enteries = list()
        #st.markdown("""<h4> Please Enter the values for the following collumns </h4>""", unsafe_allow_html=True)
        with st.expander("Enter the values for the following collumns"):
            for i in variables:
                column = st.number_input(f" {i}")
                enteries.append(column)

        #st.write(np.array(enteries).reshape(1,-1))
    except:
        st.warning('Upload Data')





model = uploadModel(filename)
if st.button('Predict'):
    predicted_output = model.predict(np.array(enteries).reshape(1,-1))
    st.dataframe(enteries)
    st.write('The Predicted output is')
    st.header(predicted_output)

