from optparse import Values
import pandas as pd
from this import d
import streamlit as st
from csv import DictReader
import os
import sys

#import app components
from Components.Navbar import Navbar;
from Components.Config import Config;
from Components.functions import buildInterractiveTable

Config()
Navbar()
st.markdown("""<h1> EDA Area </h1>""", unsafe_allow_html=True)






#saving the csv file in directory
def saveFile(data):
    
    directory=os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s="\\"
    else:
        s="/"
        
    g = directory +  s + file_name
    output=data 
    if st.button("Submit"):
        try:
            # line = [line for line in open(path)]
            output.to_csv(os.path.join(f'{g}.csv'),index=False,encoding='utf8')
            st.success('Saved Successfully')
        except Exception as e:
            st.write(e)





#saving the csv file in directory
def savegridFile(data):
    
    directory=os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s="\\"
    else:
        s="/"
        
    g = directory +  s + file_name
    output=data 
    if st.button("Submit"):
        try:
            # line = [line for line in open(path)]
            output.to_csv(os.path.join(f'{g}.csv'),index=False,encoding='utf8')
            st.success('Saved Successfully')
        except Exception as e:
            st.write(e)














# uploading your dataset
#@st.cache(suppress_st_warning=True)
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



#newdata = pd.DataFrame.from_dict(line)

#st.dataframe(newdata)


try:
    menu = ['view data','size','shape','Check Datatypes','show columns','describe','mean','std','null', "count null","corr"]
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
        st.write(data.mean())
    elif option == 'Check Datatypes':
        try:
            output = data.dtypes
            frame = pd.DataFrame(output)
            st.dataframe(frame.astype('str'))
        except Exception as e:
            st.write(e)
    elif option == 'std':
        #claculating the standard deviation
        st.write("Showing `standard deviation` of various columns")
        st.dataframe(data.std())
    elif option == 'null':
        st.write("Showing Entries with no value where `marked` means true and `unmarked` means false")
        st.write(data.isnull())

    elif option =='count null':
        st.write("Showing `number` of null value in each columns")
        st.dataframe(data.isnull().sum())

    elif option =='corr':
        # checking for correlation between columns of the data set
        try:
            col1 = st.selectbox('select first column',data.columns)
            col2 = st.selectbox('select second column',data.columns)
            a = data[f"{col1}"]
            b = data[f'{col2}']
            st.write(a.corr(b))
        except:
            st.write("`No Correlation for the selected columns`")
    else:
        st.write(data)
except:
    st.error("No Data Uploaded")



file_tosave = st.selectbox('Choose the file to save visualization',('Submit Original file','Submit Edited file'))

if file_tosave == 'Submit Original file':
    st.markdown("<h3> Submiting original data",unsafe_allow_html=True) 
    if st.checkbox('Submit for visualization'):
        saveFile(data)
elif file_tosave == 'Submit Edited file':
    st.markdown("<h3> Edit your data in the frame below",unsafe_allow_html=True)
    line  = buildInterractiveTable(data)
    file = line.values()
    file = list(file)
    #next(file)
    data = file[0]
    if st.checkbox('Submit fo visualization'):
        saveFile(data)


