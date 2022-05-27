from re import A
from warnings import catch_warnings
from pandas.core.indexes.base import Index
import streamlit as st 
import pandas as pd
import Modelbuilding,EDA,Prediction,FileUpload,Home,Visualize
from streamlit_option_menu import option_menu

PAGES = {
    "Home":Home,
    "File":FileUpload,
    "Analysis":EDA,
    "Visuals":Visualize,
    "Models":Modelbuilding,
    "Predict":Prediction,
}



#st.sidebar.title('Activities')
#selection = st.sidebar.selectbox("Menu", list(PAGES.keys()))

selection = option_menu(
    menu_title=None,
    options=list(PAGES.keys()),
    icons=['house-door-fill','cloud-arrow-up-fill','graph-up-arrow','reception-4','layers-fill','question-octagon-fill'],
    orientation='horizontal',
    #styles={
        #"container": {"padding": "0px","background-color": "red","boader-size":"25px"},
        #"icon": {"color": "orange","font-size": "25px"},
        #"nav-link": {
            #"font-size": "15px",
            #"text_align": "center",
           # "margin": "0px",
            #"--hover-color": "#eee",
           # "color":"white",
        #},
        #"na-link-selected" : {"background":"green"},
        
#    }
)
page = PAGES[selection]
page.app()
