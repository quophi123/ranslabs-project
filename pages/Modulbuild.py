import streamlit as st
from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()

st.header('Build Model Here')
options = st.radio('select',('home','school'))
st.write('<style>div.row-widget.stRadio> div{flex-direction:row;}</style>',unsafe_allow_html=True)