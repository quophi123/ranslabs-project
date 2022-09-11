#importing packages
import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk
import os
import sys
#import app components
from Components.Navbar import Navbar;
from Components.Config import Config;




Config()

Navbar()

st.markdown("""<h1> Prediction  Area </h1>""", unsafe_allow_html=True)



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

name = filename.split('.')
name.pop(0)


def uploadModel():
    # load the model from disk
    loaded_model = pk.load(open(filename, 'rb'))
    return loaded_model



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

    st.write(np.array(enteries).reshape(1,-1))
except:
    st.warning('Upload Data')





model = uploadModel()

if st.button('Predict'):
    predeicted_output = model.predict(np.array(enteries).reshape(1,-1))
    st.write('The Predicted plant is')
    st.header(predeicted_output)
    #st.write(type(model))
