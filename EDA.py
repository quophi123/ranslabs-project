from pandas import options
import streamlit as st
import pandas as pd
import numpy as np








class EploratoryDataAnalysis:

    def analyze_data(self,option,data=None):
        if  option == 'view data':
            view_type = st.sidebar.selectbox('select view type',('by rows','by columns'))
            if view_type == 'by rows':
                view_option = st.sidebar.selectbox('select view type',('head','tail','preferred number'))
                if view_option == 'head':
                    data = data.head()
                elif view_option == 'tail':
                    data = data.tail()
                else:
                    number = st.slider('slide to your preferred number',min_value=1,max_value=data.shape[0])
                    data = data.head(number)
            else:
                column_view = st.multiselect('showing data by columns',data.columns)
                data = data[column_view]
        elif option == 'size':
            data = data.size
        elif option == 'describe':
            data = data.describe()
        elif option == 'shape':
            data = data.shape
            #st.write('dataset has {} columns and {} rows'.format(data.shape[0],data.shape[1]))
        elif option == 'mean':
        
            data = data.mean()
        elif option == 'std':
            data = data.std()
        elif option == 'null':
            data = data.isnull()
        elif option =='count null':
            data = data.isnull().sum()
        else:
            return st.write(option)
        return st.write(data)

