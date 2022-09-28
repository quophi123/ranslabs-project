from optparse import Values
import pandas as pd
import numpy as np
from this import d
import streamlit as st
from csv import DictReader
# import io
import os
import sys
#from awesome_table import AwesomeTable
import csv

# import app components
from Components.Navbar import Navbar;
from Components.Config import Config;
from Components.functions import buildInterractiveTable
from Components.frame import filter_dataframe

Config()
Navbar()
st.markdown("""<h1>Analyze your data here </h1>""", unsafe_allow_html=True)


st.markdown('''
        <style>
        div.css-1a65djw.e1tzin5v0{border-color:red}
        div.css-1a65djw{border-radius:5em}
        </style>
''', unsafe_allow_html=True)


# saving the csv file in directory
def saveFile(data):
    directory = os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s = "\\"
    else:
        s = "/"

    g = directory + s + file_name
    output = data
    try:
        # line = [line for line in open(path)]
        output.to_csv(os.path.join(f'{g}.csv'), index=False, encoding='utf8')
        st.success('Saved Successfully')
    except Exception as e:
        st.write(e)


# saving the csv file in directory
def savegridFile(data):
    directory = os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s = "\\"
    else:
        s = "/"

    g = directory + s + file_name
    output = data
    if st.button("Submit"):
        try:
            # line = [line for line in open(path)]
            output.to_csv(os.path.join(f'{g}.csv'), index=False, encoding='utf8')
            st.success('Saved Successfully')
        except Exception as e:
            st.write(e)


# uploading your dataset
# @st.cache(suppress_st_warning=True)
def file():
    k = ['csv', 'xlsx', 'json']
    data = st.file_uploader('Upload file here', type=k)
    st.write(data)
    if data is not None:
        df = pd.read_csv(data)
    else:
        df = st.warning("Upload Data")
    return df


# def uploadJson():
#     json_data = st.file_uploader('upload your json file', type=['json'])
#     return json_data
#
#
# json_file = uploadJson()
# st.write(json_file)

data = file()

try:
    menu = ['view data', 'size', 'shape', 'Check Datatypes', 'show columns', 'describe', 'mean', 'std', 'null',
            "count null", "corr"]
    option = st.selectbox('Select EDA to perform', menu, help='select type of eda')

    if option == 'view data':
        view_type = st.selectbox('select view type', ('by rows', 'by columns'))
        if view_type == 'by rows':
            with st.expander("Choose view options..."):
                view_option = st.radio('select view type', ('', 'head', 'tail', 'preferred number'), horizontal=True)

            if view_option == 'head':
                st.table(data.head())
            elif view_option == 'tail':
                st.table(data.tail())
            elif view_option == 'preferred number':
                number = st.slider('slide to your preferred number', min_value=1, max_value=data.shape[0])
                st.table(data.head(number))
            else:
                pass
        else:
            column_view = st.multiselect('showing data by columns', data.columns)
            st.table(data[column_view])

    elif option == 'size':
        st.write(f'The size of your data is {data.size}')

    elif option == 'show columns':
        st.write(f'Your dataset has {len(data.columns)} columns as shown below')
        st.dataframe(data.columns)

    elif option == 'describe':
        st.write('Brief information about your data')
        try:
            st.dataframe(data.describe())
        except Exception as e:
            st.warning('This data type cannot be described')
            

    elif option == 'shape':
        st.write('dataset has `{}` columns and `{}` rows'.format(data.shape[0], data.shape[1]))

    elif option == 'mean':
        # calculating for mean of the dataset
        st.write(data.mean())
    elif option == 'Check Datatypes':
        try:
            output = data.dtypes
            frame = pd.DataFrame(output)
            st.write('Your columns has the following data types')
            st.dataframe(frame.astype('str'))
        except Exception as e:
            st.write(e)

    elif option == 'std':
        # claculating the standard deviation
        st.write("Showing `standard deviation` of various columns")
        st.dataframe(data.std())
    elif option == 'null':
        st.write("Showing Entries with no value where `marked` means true and `unmarked` means false")
        st.write(data.isnull())

    elif option == 'count null':
        st.write("Showing `number` of null value in each columns")
        st.dataframe(data.isnull().sum())

    elif option == 'corr':
        # checking for correlation between columns of the data set
        try:
            col1 = st.selectbox('select first column', data.select_dtypes(include = "float64").columns)
            col2 = st.selectbox('select second column', data.select_dtypes(include = "float64").columns)
            a = data[f"{col1}"]
            b = data[f'{col2}']
            st.write(a.corr(b))
        except:
            st.write("`No Correlation for the selected columns`")
    else:
        st.write(data)
except:
    st.error("No Data Uploaded")

with st.expander('view all data'):
    try:
        df = pd.DataFrame(data)
        table_type = st.selectbox('table_type', ('table with scrol', 'table with no scrol'))
        if table_type == 'table with scrol':
            st.dataframe(filter_dataframe(df))
        else:
            st.table(filter_dataframe(df))
        # AwesomeTable(df,show_order=True,show_search=True)
    except Exception as e:
        st.write(e)

file_tosave = st.selectbox('Choose the file to save for visualization', ('Save Original file', 'Edited file'))

if file_tosave == 'Save Original file':
    st.markdown("<h3> Submiting original data for visualization </h3>", unsafe_allow_html=True)
    if st.button('Submit for visualization'):
        saveFile(data)
elif file_tosave == 'Edited file':
    edit_type = st.radio('Edit Type', ('Edit with new value', 'Drop Values', 'replace'), horizontal=True)
    if edit_type == 'Edit with new value':
        st.markdown("<h3> Edit your data in the frame below", unsafe_allow_html=True)
        line = buildInterractiveTable(data)
        file = line.values()
        file = list(file)
        # next(file)
        data = file[0]
    elif edit_type == 'Drop Values':
        data = data.dropna(axis=0)
        st.write('Null value after droping')
        st.write(data.isnull().sum())
    else:
        replace = st.selectbox('Select replace type', ('mean', 'standard deviation', 'zeros'))
        if replace == 'mean':
            mean = data.mean()
            st.write(mean)
            data = data.fillna(value=mean, axis=0)
        elif replace == 'standard deviation':
            std = data.std()
            st.write(std)
            data = data.fillna(value=std, axis=0)
        else:
            data = data.fillna(value=0, axis=0)
        st.dataframe(data)
    if st.button('Submit'):
        saveFile(data)
