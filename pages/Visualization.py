from xml.etree.ElementInclude import include
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sweetviz as sv
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
import numpy as np
import time
from csv import DictReader
import os.path
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()
Navbar()
st.markdown("""<h1> Data Visualization Area </h1>""", unsafe_allow_html=True)




#uploading the saved file
#def uploadFile():
    #try:
        #rows = []
        #file = open('C:/Users/quophi/Desktop/Main Folder/Projects/final project/ranslabs-project/newfilenan.csv', 'r', encoding='utf8')
        #csvreader = DictReader(file)
        #table = []
        #for row in csvreader:
            #float_row = {}
            #for column in row:
                #float_row[column] = row[column]
            #table.append(float_row)
        #file.close()
        #data = pd.DataFrame(table)
    #except Exception as e:
        #st.write(e)
    #return data
 

data = pd.read_csv('newfile.csv')


with st.expander('Select an option'):
    option = st.selectbox('Choose an activity',('','Auto Generate Plots','Custom Plots'))







if option == ('Auto Generate Plots'):
    st.markdown("""<h3> Automatically generating a plot for you </h3>""", unsafe_allow_html=True)
    if st.button('Generate Chart'):
        with st.spinner(text='Wait while we generate your chart....'):
            time.sleep(0.5)
            report = data.profile_report()
        st.success('Done') 
        st_profile_report(report,navbar=False)


        report = sv.analyze(data)
        report.show_html('Report.html')


#charts = ['Line Chart','Pair Plots','Heat Map','Bar Chart','Box Plot']
elif option == ('Custom Plots'):
        
    charts = ['Tree map','Pie Chart','Line Chart','Pair Plots','Heat Map','Bar Chart','Box Plot','Scatter Plot']
    chart_type=st.radio('select your prefered algorithm',charts,horizontal=True)





    if chart_type == 'Pair Plots':
        st.markdown("""<h3> Pair Ploting </h3>""", unsafe_allow_html=True)
        hue = st.selectbox('Select your target value values...',data.columns)
        if st.button('Generate chart'):
            fig = sns.pairplot(data, hue=hue)
            st.pyplot(fig)
            plot = px.scatter_matrix(data, dimensions=data.columns, color=hue)
            st.plotly_chart(plot)
    elif chart_type == 'Pie Chart':
        st.markdown("""<h3> Pie Chart </h3>""", unsafe_allow_html=True)
        x = st.selectbox('Select your x values...',data.select_dtypes(include = "object").columns)
        y = st.selectbox('Select your y values...',data.select_dtypes(include = "float64").columns)
        if st.button('Generate chart'):
            fig = px.pie(data, values=y, names=x)
            st.plotly_chart(fig)


    elif chart_type == 'Line Chart':
        st.markdown("""<h3> Line Chart </h3>""", unsafe_allow_html=True)
        x = st.selectbox('Select your x-axis values...',data.select_dtypes(include = "float64").columns)
        y = st.selectbox('Select your y-axis values...',data.select_dtypes(include = "float64").columns)
        plot = px.line(data, x=data[f'{x}'],y=data[f'{y}'],title=f'{x} vs {y}')
        st.plotly_chart(plot)

    elif chart_type == 'Heat Map':
        st.markdown("""<h3> Heat Map </h3>""", unsafe_allow_html=True)
        if st.button('Generate Plot'):
            with st.spinner(text='Wait while we generate your chart....'):
                time.sleep(0.5)
            st.success('Done')
            corr = data.corr()
            st.write(sns.heatmap(data, annot=True))
           








    elif chart_type == 'Bar Chart':
    #with tab4:
        st.markdown("""<h3> Bar Chart </h3>""", unsafe_allow_html=True)
        x = st.selectbox('Select your x values...',data.columns)
        y = st.selectbox('Select your y values...',data.columns)
        target = st.selectbox('Select your target values...',data.select_dtypes(include = "object").columns)
        if st.button('Generate Plot'):
            with st.spinner(text='Wait while we generate your chart....'):
                time.sleep(1)
            st.success('Done')
            fig = px.bar(data, x=x, y=y, color=target, barmode='group',hover_data=[x, y])
            st.plotly_chart(fig)





    elif chart_type == 'Box Plot':
        st.markdown("""<h3> Box Plot </h3>""", unsafe_allow_html=True)
        x = st.selectbox('Select your x values...',data.select_dtypes(include = "object").columns)
        y = st.selectbox('Select your y values...',data.select_dtypes(include = "float64").columns)
        with st.spinner(text='Wait while we generate your chart....'):
            time.sleep(0.5)
        if st.button('Generate Plot'):
            st.success('Done')
            plot = px.box(data, x=data[f'{x}'], y=data[f'{y}'],hover_data=[x, y])
            st.plotly_chart(plot)



    elif chart_type == 'Scatter Plot':
        st.markdown("""<h3> Scatter Plot </h3>""", unsafe_allow_html=True)
        x = st.selectbox('Select your x values...',data.select_dtypes(include = "float64").columns)
        y = st.selectbox('Select your y values...',data.select_dtypes(include = "float64").columns)
        target = st.selectbox('Select your target values...',data.select_dtypes(include = "object").columns)
        if st.button('Generate Plot'):
            plot = px.scatter(data, x=data[f'{x}'], y=data[f'{y}'],color=target,size=data[f'{x}'],
                 hover_name=target, log_x=True, size_max=10,hover_data=[x, y])
            st.plotly_chart(plot)



