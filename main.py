from re import A
from warnings import catch_warnings
from pandas.core.indexes.base import Index
import streamlit as st 
import pandas as pd
from PIL import Image
#import Modelbuilding,EDA,Prediction,FileUpload,Home,Visualize
#from streamlit_option_menu import option_menu


#site configurations 
logo = Image.open('logo.jpg')
st.set_page_config(page_title='ml automate', page_icon=logo)

hid_menu_style = """
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            </style>
"""
st.markdown(hid_menu_style,unsafe_allow_html=True)





st.header('main')
#PAGES = {
 #   "Home":Home,
 #   "Analysis":EDA,
 #   "Visuals":Visualize,
 #   "Models":Modelbuilding,
 #   "Predict":Prediction,
#}



#st.sidebar.title('Activities')
#selection = st.sidebar.selectbox("Menu", list(PAGES.keys()))

#selection = option_menu(
    #menu_title=None,
    #options=list(PAGES.keys()),
    #icons=['house-door-fill','cloud-arrow-up-fill','graph-up-arrow','reception-4','layers-fill','question-octagon-fill'],
    #orientation='horizontal',
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
#)
#page = PAGES[selection]
#page.app()
