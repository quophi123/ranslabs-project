#importing packages
import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk
#import app components
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()

st.markdown("""<h1> Prediction  Area </h1>""", unsafe_allow_html=True)

filename = 'sepal_length-sepal_width-petal_length-petal_width-.sav'
name = filename.split('-')



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
    st.markdown("""<h4> Please Enter the values for the following collumns </h4>""", unsafe_allow_html=True)
    for i in variables:
        column = st.number_input(f" {i}")
        enteries.append(column)

    st.write(np.array(enteries).reshape(1,-1))
except:
    st.warning('Upload Data')



model = uploadModel()
predeicted_output = model.predict(np.array(enteries).reshape(1,-1))
if st.button('Predict'):
    st.header('The Predicted plants is')
    st.dataframe(predeicted_output)
    #st.write(type(model))
