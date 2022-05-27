import streamlit as st
import pandas as pd
import numpy as np



def app():
    chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
    st.area_chart(chart_data)


    
    df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(df)