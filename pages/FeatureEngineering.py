from sklearn.preprocessing import LabelEncoder,OneHotEncoder,OrdinalEncoder
import streamlit as st 
import pandas as pd
import numpy as np
import os
import sys



#import app Components
from Components.Navbar import Navbar;
from Components.Config import Config;


#inintializing site components and configurations
Config()
Navbar()


#functions
def saveFile(data):
    
    directory=os.getcwd()
    file_name = 'newfile'
    s = None
    platform = sys.platform.startswith('win')
    if platform == True:
        s="\\"
    else:
        s="/"
        
    g = directory +  s + file_name
    output=data
    if st.button('Save Encoded Data'): 
        try:
            # line = [line for line in open(path)]
            output.to_csv(os.path.join(f'{g}.csv'),index=False,encoding='utf8')
            st.success('Saved Successfully')
        except Exception as e:
            st.write(e)




st.markdown('<h3> Perform Feature Engineering Here</h3>',unsafe_allow_html=True)


#file = pd.read_csv('newfile.csv')
try:
    data = pd.read_csv('newfile.csv')
except Exception as es:
    st.warning('No data uploaded')
encoding_type = st.selectbox('Select your encoding type',('🏷️Label Encoder','♨️OneHot Encoder'))

if encoding_type == '🏷️Label Encoder':
    with st.expander('Encoding your data with label encoder'):
        st.markdown('''<p>LabelEncoder can be used to normalize labels. It can also be used to transform non-numerical labels 
        (as long as they are hashable and comparable) to numerical labels.</p>''',unsafe_allow_html=True)

        columns_to_encode = st.multiselect('Select the columns you want ot encode',data.select_dtypes(include = "object").columns)
        re_coder = data
        le = LabelEncoder()
        ordinal = OrdinalEncoder()
        #encode_type = st.multiselect('Select the columns you want ot encode',('Encode Features','Encode Target'))
        for column in columns_to_encode:
            data[column] = le.fit_transform(data[column])
            #data[column] = ordinal.fit_transform(data[column])
        st.table(data)
        saveFile(data)

elif encoding_type == '♨️OneHot Encoder':
    with st.expander('Encoding your data with one-hot encoding'):
        st.markdown('''<p>One-Hot Encoding is another popular technique for treating categorical variables. It simply creates additional features based on the number of unique values in these
         categorical feature. Every unique value in the category will be added as a feature.</p>''',unsafe_allow_html=True)
        #st.subheader('OneHot Encode Here')
        #columns_to_encode = st.multiselect('Select the columns you want ot encode',data.select_dtypes(include = "object").columns)
        oneHot = OneHotEncoder()
        data = pd.get_dummies(data)
        st.table(data)
        saveFile(data)
        
