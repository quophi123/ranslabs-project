from tkinter.font import names
import streamlit as st
from pytz import NonExistentTimeError
import pandas as pd
import numpy as np
import io
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle as pk
from pathlib import Path
import sys
from sklearn.model_selection import cross_val_score, StratifiedKFold, KFold
# import functions
from Components.functions import Modelbuilding

from Components.Navbar import Navbar;
from Components.Config import Config;

Config()
Navbar()

st.markdown("""<h1> Build your model here  </h1>""", unsafe_allow_html=True)


def getColumnName(features_columns):
    # cols = saveColumns()
    cols = features_columns
    name = ''
    for i in range(len(cols)):
        name = name + "." + cols[i]
    return name


def downloadModel(model, name):
    # save the model to disk
    path = str(Path.home() / "Downloads")
    platform = sys.platform.startswith('win')
    if platform == True:
        s = "\\"
    else:
        s = "/"
    namefile = path + s + name
    pk.dump(model, open(f"{namefile}.sav", 'wb'))


def saveModel(model, model_name):
    # save the model to disk
    path = 'C:/Users/quophi/Desktop/Main Folder/Projects/final project/ranslabs-project/'

    filename = path + model_name
    pk.dump(model, open(f"{filename}.sav", 'wb'))


def build():
    try:

        data = pd.read_csv('newfile.csv')
        columns = data.columns

        # models function
        def supportVectorMachine():
            with st.expander("Choose parameters"):
                st.markdown(
                    """
                            This section allows you to sselect your prefered parameter for the selected 
                            algorithm, for building your model.""", unsafe_allow_html=True
                )
                params = dict()
                C = st.slider("C", min_value=1, max_value=10)
                params.update({"C": C})
                random_state = st.slider("random_state", 1, 5)
                params.update({"random_state": random_state})
                kernel = st.radio("kernel", ('rbf', 'poly', 'linear', 'sigmoid'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"kernel": kernel})
                gamma = st.radio("gamma", ('scale', 'auto'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"gamma": gamma})
                verbose = st.radio("verbose", (True, False))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"verbose": verbose})
            return params

        def randomForest():
            with st.expander("Choose parameters"):
                st.markdown(
                    """
                            This section allows you to sselect your prefered parameter for the selected 
                            algorithm, for building your model.""", unsafe_allow_html=True
                )
                params = dict()
                n_estimators = st.slider("Select Number of estimators", min_value=1, max_value=100)
                params.update({"n_estimators": n_estimators})
                max_depth = st.slider("Select maximum dept", 10)
                params.update({"max_depth": max_depth})
                min_samples_split = st.slider("minimun sample split", 2, 10)
                params.update({"min_samples_split": min_samples_split})
                min_samples_leaf = st.slider("min_samples_leaf", 1, 10)
                params.update({"min_samples_leaf": min_samples_leaf})
                max_features = st.radio("max_features", ('auto', 'sqrt', 'log2'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"max_features": max_features})
                random_state = st.slider("random_state", 1, 5)
                params.update({"random_state": random_state})

            return params

        def decisionTree():
            with st.expander("Choose parameters"):
                st.markdown(
                    """
                            This section allows you to sselect your prefered parameter for the selected 
                            algorithm, for building your model.""", unsafe_allow_html=True
                )
                params = dict()
                splitter = st.radio("splitter", ('best', 'random'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"splitter": splitter})
                max_depth = st.slider("Select maximum dept", 10)
                params.update({"max_depth": max_depth})
                min_samples_split = st.slider("minimun sample split", 2, 10)
                params.update({"min_samples_split": min_samples_split})
                min_samples_leaf = st.slider("min_samples_leaf", 1, 10)
                params.update({"min_samples_leaf": min_samples_leaf})
                max_features = st.radio("max_features", ('auto', 'sqrt', 'log2'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"max_features": max_features})
                random_state = st.slider("random_state", 1, 5)
                params.update({"random_state": random_state})
                max_leaf_nodes = st.slider("max_leaf_nodes", min_value=2, max_value=10)
                params.update({"max_leaf_nodes": max_leaf_nodes})

            return params

        def kNearestNeibhor():
            with st.expander("Choose parameters"):
                st.markdown(
                    """
                            This section allows you to sselect your prefered parameter for the selected 
                            algorithm, for building your model.""", unsafe_allow_html=True
                )
                params = dict()
                n_neighbors = st.slider("n_neighbors", min_value=3, max_value=10)
                params.update({"n_neighbors": n_neighbors})
                weights = st.radio("weights", ('uniform', 'distance'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"weights": weights})
                algorithm = st.radio("algorithm", ('auto', 'ball_tree', 'kd_tree', 'brute'))
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                params.update({"algorithm": algorithm})
                leaf_size = st.slider("leaf_size", 30, 100)
                params.update({"leaf_size": leaf_size})

            return params

        list_of_models = ['RandomForest', 'DecisionTree', 'KNearestNeibhor', 'SupportVectorMachine']
        algorithm = st.radio('select your prefered algorithm', list_of_models)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        test_size = st.slider('Select the size of your test data', (10.0 / 100), (50.0 / 100), step=.05)

        with st.expander("Select Your Features and Labels"):
            st.markdown(
                """
                Features are the independent variables for building your model and the
                Targets are the dependent variable, ie the variables to be predicted """, unsafe_allow_html=True
            )
            features_columns = st.multiselect("Select your Features Columns", data.columns,
                                              help='Select the columns you want to use as features')
            labels_columns = st.selectbox("Select your labels/Targets Columns", data.columns,
                                          help='Select the columns you want to use as labels')

        name = getColumnName(features_columns)

        features = data[features_columns]
        labels = data[labels_columns]
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=test_size)

        # building the model with randomforestclassifier
        models = []
        models.append(('SVC', SVC()))
        models.append(('RF', RandomForestClassifier()))
        models.append(('DT', DecisionTreeClassifier()))
        models.append(('KNN', KNeighborsClassifier()))

        results = list()
        std = list()
        mean = list()
        for name, model in models:
            kfold = KFold(n_splits=10, random_state=None)
            cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='accuracy')

            results.append(name)
            std.append(cv_results.std())
            mean.append(cv_results.mean())

        cross_validations_output = list(zip(results, mean, std))
        df = pd.DataFrame(cross_validations_output, columns=['Model', 'Mean', 'Std'])
        with st.expander('Perform cross validation score for your data on available model'):
            st.markdown("""NOTE:
                cross-validation uses several data subset to evaluate and train a model across a number of iterations
                A model is typically given a dataset of known data for 
                training purposes (training dataset) and a dataset of unknown data (or first seen data) 
                for testing purposes in a prediction issue (called the validation dataset or testing set). 
                Cross-validation aims to identify issues like overfitting or selection bias and to provide 
                insight into how the model will generalize to an independent dataset by testing the models 
                propensity to predict fresh data that was not included in its estimation.""", unsafe_allow_html=True)
            st.write(df)

        try:
            if algorithm == "RandomForest":
                params = randomForest()
                clf = Modelbuilding.randomForestClassifier(features=features, labels=labels, params=params,
                                                           X_train=X_train, X_test=X_test, y_train=y_train,
                                                           y_test=y_test)
                if st.button('Save Model'):
                    try:
                        saveModel(model=clf, model_name=name)
                        st.success('Model saved')
                    except Exception as e:
                        st.error(e)


            # building the model with decisionTreeClassifier
            elif algorithm == "DecisionTree":
                params = decisionTree()
                clf = Modelbuilding.decisionTreeClassifier(features=features, labels=labels, params=params,
                                                           X_train=X_train, X_test=X_test, y_train=y_train,
                                                           y_test=y_test)

                if st.button('Save Model'):
                    try:
                        saveModel(model=clf, model_name=name)
                        st.success('Model saved')
                    except Exception as e:
                        st.error('Error is saving model')


            # builds model with knearstNeighborClassifier
            elif algorithm == "KNearestNeibhor":
                params = kNearestNeibhor()
                clf = Modelbuilding.knearstNeighborClassifier(features=features, labels=labels, params=params,
                                                              X_train=X_train, X_test=X_test, y_train=y_train,
                                                              y_test=y_test)

                if st.button('Save Model'):
                    try:
                        saveModel(model=clf, model_name=name)
                        st.success('Model saved')
                    except Exception as e:
                        st.error('Error is saving model')

            elif algorithm == "SupportVectorMachine":
                params = supportVectorMachine()
                clf = Modelbuilding.supportVectorMachine(features=features, labels=labels, params=params,
                                                         X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

                if st.button('Save Model'):
                    try:
                        saveModel(model=clf, model_name=name)
                        st.success('Model saved')
                    except Exception as e:
                        st.error('Error is saving model')

        except (RuntimeError, TypeError, NameError) as e:
            st.warning('Select your features')
        return clf
    except Exception as e:

        st.warning('Select your features and labels')
    # st.stop()


# initialize the build model function
clf = build()

with st.expander("Do You Want to download your model?"):
    name = st.text_input('Enter the name of your file')
    if st.button('Download Model'):
        try:
            # calling the download function
            downloadModel(model=clf, name=name)
            st.success("Downloaded model successfully check your download folder")
        except Exception as e:
            st.error(e)
