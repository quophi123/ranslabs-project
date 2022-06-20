from pytz import NonExistentTimeError
import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#import functions
from functions import Modelbuilding


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


st.subheader("Build Your Models Here")



def file():
    k =['csv','xlsx']
    data = st.file_uploader('Upload file here',type=k)
    #data = pd.to_csv(data)
    if data is not None:
        df = pd.read_csv(data)
    else:
        df = st.warning("Upload Data")
    return df


data = file()










#models function
def supportVectorMachine():
    params = dict()
    C = st.slider("C",min_value=1,max_value=10)
    params.update({"C":C})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    kernel = st.radio("kernel",('rbf','poly', 'linear','sigmoid'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"kernel":kernel})
    gamma = st.radio("gamma",('scale','auto'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"gamma":gamma})
    verbose = st.radio("verbose",(True,False))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"verbose":verbose})
    return params
        

def randomForest():  
    params = dict()
    n_estimators = st.slider("Select Number of estimators",min_value=1,max_value=100)
    params.update({"n_estimators":n_estimators})
    max_depth = st.slider("Select maximum dept",10)
    params.update({"max_depth":max_depth})
    min_samples_split = st.slider("minimun sample split",2,10)
    params.update({"min_samples_split":min_samples_split})
    min_samples_leaf = st.slider("min_samples_leaf",1,10)
    params.update({"min_samples_leaf":min_samples_leaf})
    max_features = st.radio("max_features",('sqrt','log', 'None'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"max_features":max_features})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    st.write(params['n_estimators'])
    return params

def decisionTree():
    params = dict()
    splitter = st.radio("splitter",('best','random'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"splitter":splitter})
    max_depth = st.slider("Select maximum dept",10)
    params.update({"max_depth":max_depth})
    min_samples_split = st.slider("minimun sample split",2,10)
    params.update({"min_samples_split":min_samples_split})
    min_samples_leaf = st.slider("min_samples_leaf",1,10)
    params.update({"min_samples_leaf":min_samples_leaf})
    max_features = st.radio("max_features",('auto','sqrt','log', 'None'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"max_features":max_features})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    max_leaf_nodes = st.slider("max_leaf_nodes",min_value=2,max_value=10)
    params.update({"max_leaf_nodes":max_leaf_nodes})
    
    return params
    

def kNearestNeibhor():
   
    params = dict()
    n_neighbors = st.slider("n_neighbors",min_value=3,max_value=10)
    params.update({"n_neighbors":n_neighbors})
    weights = st.radio("weights",('uniform','distance'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"weights":weights})
    algorithm = st.radio("algorithm",('auto','ball_tree','kd_tree','brute'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
    params.update({"algorithm":algorithm})
    leaf_size = st.slider("leaf_size",30,100)
    params.update({"leaf_size":leaf_size})
        
    return params





















list_of_models = ['RandomForest','DecisionTree','KNearestNeibhor','SupportVectorMachine']
algorithm=st.sidebar.selectbox('select your prefered algorithm',list_of_models)

test_size = st.slider('Select the size of your test data',(10.0/100),(50.0/100),step=.05)


features_columns = st.multiselect("Select your festures for the model",data.columns)
labels_columns = st.selectbox("Select your labels for the model",data.columns)

features = data[features_columns]
labels = data[labels_columns]
X_train,X_test,y_train,y_test = train_test_split(features,labels, test_size=test_size)




if algorithm == "RandomForest":
    params = randomForest()
    Modelbuilding.randomForestClassifier(features=features,labels=labels,params=params,
                                        X_train=X_train,y_train=y_train,y_test=y_test)
    


elif algorithm == "DecisionTree":
    params = decisionTree()
    Modelbuilding.decisionTreeClassifier(features=features,labels=labels,params=params,
                                        X_train=X_train,y_train=y_train,y_test=y_test)




elif algorithm == "KNearestNeibhor":
    params = kNearestNeibhor()
    Modelbuilding.knearstNeighborClassifier(features=features,labels=labels,params=params,
                                        X_train=X_train,y_train=y_train,y_test=y_test)



elif algorithm == "SupportVectorMachine":
   params = supportVectorMachine()
   Modelbuilding.supportVectorMachine(features=features,labels=labels,params=params,
                                        X_train=X_train,y_train=y_train,y_test=y_test)


