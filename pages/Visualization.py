import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
import numpy as np
import time
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()
st.markdown("""<h1> Data Visualization Area </h1>""", unsafe_allow_html=True)



@st.cache(suppress_st_warning=True)
def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    return df

data = file()


with st.expander('Select an option'):
    option = st.selectbox('Choose an activity',('','Auto Generate Plots','Custom Generate'))


if option == ('Auto Generate Plots'):
    st.markdown("""<h3> Automatically generating a plot for you </h3>""", unsafe_allow_html=True)
    if st.button('Generate Chart'):
        with st.spinner(text='Wait while we generate your chart....'):
            time.sleep(10)
        st.success('Done') 
        report = data.profile_report()
        st_profile_report(report,navbar=False)



elif option == ('Custom Generate'):
        
    charts = ['Line Chart','Pair Plots','Heat Map','Bar Chart','Box Plot']
    chart_type=st.radio('select your prefered algorithm',charts)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)

    if chart_type == 'Pair Plots':
        st.markdown("""<h3> Pair Ploting </h3>""", unsafe_allow_html=True)
        if st.button('Generate Plot'):
            with st.spinner(text='Wait while we generate your chart....'):
                time.sleep(10)
            st.success('Done')
            fig = sns.pairplot(data, hue="species")
            st.pyplot(fig)
    elif chart_type == 'Line Chart':
        st.markdown("""<h3> Line Chart </h3>""", unsafe_allow_html=True)


    elif chart_type == 'Heat Map':
        st.markdown("""<h3> Heat Map </h3>""", unsafe_allow_html=True)
        c = st.multiselect('sl',data.columns)
        if st.button('Generate Plot'):
            with st.spinner(text='Wait while we generate your chart....'):
                time.sleep(10)
            st.success('Done')
            fig, ax = plt.subplots()
            sns.heatmap(file().corr(), ax=ax)
            st.write(fig)


    elif chart_type == 'Bar Chart':
        st.markdown("""<h3> Bar Chart </h3>""", unsafe_allow_html=True)


    elif chart_type == 'Box Plot':
        st.markdown("""<h3> Box Plot </h3>""", unsafe_allow_html=True)
        c = st.multiselect('sl',data.columns)
        if st.button('Generate Plot'):
            with st.spinner(text='Wait while we generate your chart....'):
                time.sleep(10)
            st.success('Done')
            fig = px.box(data_frame=data[c])
            st.write(fig)




