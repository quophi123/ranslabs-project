import streamlit as st
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()
st.markdown("""<h1> Data Visualization Area </h1>""", unsafe_allow_html=True)