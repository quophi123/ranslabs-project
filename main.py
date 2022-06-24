
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()


st.markdown("""<h1> Home Area </h1>""", unsafe_allow_html=True)
st.snow()

#  st.sidebar.selectbox('Choose an option',('main','home','school'))


def load_lottiefiles(filepath: str):
    with open(filepath, 'r') as file:
        return json.load(file)


#def load_lottievideo(url: str):
    #r = requests.get(url)
    #if r.status_code != 200:
        #return  None
    #return r.json()

lottie = load_lottiefiles("assets/dataanalytics.json")
#lottie_video = load_lottievideo("https://iconscout.com/lottie/data-analytics-information-presentation-3914375")
st_lottie(
    lottie,
    height=300,
    loop=False,
    quality='high',
    
)


#st_lottie(lottie_video(), key='helo')


#st.video("assets/da.mp4")



# uploading your dataset

def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    return df


try:
    

    data = file()
    report = data.profile_report()

    st_profile_report(report,navbar=False)
except Exception as e:
    st.warning('Please Upload your data')

    from streamlit_ace import st_ace

    # Spawn a new Ace editor
    content = st_ace()

    # Display editor's content as you type
    content