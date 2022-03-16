import streamlit as st
import pandas as pd



class UploadFile:
        
    def file_upload(self,data):
            data = st.file_uploader('Upload file here',('csv','xlsx'))
            if data is not None:
                df = pd.read_csv(data)
            return df
        