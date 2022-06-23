import streamlit as st
from pytz import NonExistentTimeError
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#import functions
from Components.functions import Modelbuilding






from Components.Navbar import Navbar;
from Components.Config import Config;



Config()

Navbar()
st.markdown("""<h1> Model Building Area </h1>""", unsafe_allow_html=True)

try:
    
    data = pd.read_csv('newfile.csv')
    columns = data.columns



    #models function
    def supportVectorMachine():
        with st.expander("Choose parameters"):
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
        with st.expander("Choose parameters"):  
            params = dict()
            n_estimators = st.slider("Select Number of estimators",min_value=1,max_value=100)
            params.update({"n_estimators":n_estimators})
            max_depth = st.slider("Select maximum dept",10)
            params.update({"max_depth":max_depth})
            min_samples_split = st.slider("minimun sample split",2,10)
            params.update({"min_samples_split":min_samples_split})
            min_samples_leaf = st.slider("min_samples_leaf",1,10)
            params.update({"min_samples_leaf":min_samples_leaf})
            max_features = st.radio("max_features",('auto','sqrt','log2'))
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
            params.update({"max_features":max_features})
            random_state = st.slider("random_state",1,5)
            params.update({"random_state":random_state})
            
        return params

    def decisionTree():
        with st.expander("Choose parameters"):
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
            max_features = st.radio("max_features",('auto','sqrt','log2'))
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
            params.update({"max_features":max_features})
            random_state = st.slider("random_state",1,5)
            params.update({"random_state":random_state})
            max_leaf_nodes = st.slider("max_leaf_nodes",min_value=2,max_value=10)
            params.update({"max_leaf_nodes":max_leaf_nodes})
        
        return params
        

    def kNearestNeibhor():
        with st.expander("Choose parameters"):
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
    algorithm=st.radio('select your prefered algorithm',list_of_models)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html = True)
      

    test_size = st.slider('Select the size of your test data',(10.0/100),(50.0/100),step=.05)

    with st.expander("Select Your Features and Labels"):
        features_columns = st.multiselect("Select your festures for the model",data.columns,help='Select the columns you want to use as features')
        labels_columns = st.selectbox("Select your labels for the model",data.columns,help='Select the columns you want to use as labels')
    
    def saveColumns():
        return features_columns

    


    features = data[features_columns]
    labels = data[labels_columns]
    X_train,X_test,y_train,y_test = train_test_split(features,labels, test_size=test_size)

    if algorithm == "RandomForest":
        params = randomForest()
        Modelbuilding.randomForestClassifier(features=features,labels=labels,params=params,
                                            X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)
        


    elif algorithm == "DecisionTree":
        params = decisionTree()       
        Modelbuilding.decisionTreeClassifier(features=features,labels=labels,params=params,
                                            X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)




    elif algorithm == "KNearestNeibhor":
        params = kNearestNeibhor()
        Modelbuilding.knearstNeighborClassifier(features=features,labels=labels,params=params,
                                            X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)



    elif algorithm == "SupportVectorMachine":
        params = supportVectorMachine()
        Modelbuilding.supportVectorMachine(features=features,labels=labels,params=params,
                                                X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)

except (RuntimeError, TypeError, NameError) as e:
    st.stop()
   
