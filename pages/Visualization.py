import streamlit as st
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()
st.header('Visualization Area')


st.button('click me')

st.multiselect('Choose an option',('main','home','school'))