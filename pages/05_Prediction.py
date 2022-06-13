import streamlit as st 
from PIL import Image

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


def app():
    return st.subheader('predict here')

app()
