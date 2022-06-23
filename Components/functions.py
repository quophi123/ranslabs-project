#import app and data modules
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st 
from PIL import Image
import time
import seaborn as sns
import pickle as pk

#machine leaning packages
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error


from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid import AgGrid,GridUpdateMode,JsCode
# functions 







#grid table area

def buildInterractiveTable(data):
    _select = st.sidebar.radio('select',('Highlight','Hide'))
    gd = GridOptionsBuilder.from_dataframe(data)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True,groupable=True,resizable=True)


    cel_mode = st.radio('Selection mode',options=['single','multiple'])
    gd.configure_selection(selection_mode=cel_mode,use_checkbox=True)
    gridoptions = gd.build()
    gridtable = AgGrid(data,gridOptions=gridoptions,update_mode=GridUpdateMode.SELECTION_CHANGED,
                    height=500,allow_unsafe_jscode=True,theme='fresh',allow_enterprice_modules = True)
    selected_rows = gridtable['selected_rows']
    st.header("Selected Columns")
    st.dataframe(selected_rows)









def saveModel(model,model_name):
    # save the model to disk
    path = 'C:/Users/quophi/Desktop/Main Folder/Projects/final project/ranslabs-project/'
    
    filename = path + model_name
    pk.dump(model, open(f"{filename}.sav", 'wb'))



data = pd.read_csv('newfile.csv')
columns = data.columns






class Modelbuilding:

    def randomForestClassifier(features,labels,params,X_train,X_test,y_train,y_test):
        with st.container():
            with st.form('random forest'):
                pass
                if st.form_submit_button('Submit Random Forest Parameters',help='Click this button to send your selected parameters to the model'):
                    st.success("Parameter Submitted Succesfully")
            try:
                if st.checkbox("Build"):
                    #st.write(params)
                    with st.spinner(text='Wait while your model is been buid...'):
                        time.sleep(3)
                    st.success('Done')
                    rdm = RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
                    min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'])
                    clf = rdm.fit(X_train,y_train)
                    predeicted_output = clf.predict(X_test)
                    st.header('The Predicted plants are')
                    st.dataframe(predeicted_output)
                    st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))
                    model_name = f'{columns[0]}-{columns[1]}-{columns[2]}-{columns[3]}-'
                    if st.button('Save Model'):
                        try:
                            saveModel(model=clf,model_name=model_name)
                            st.success('Model saved')
                        except Exception as e:
                            st.error('Error is saving model')
                    #st.write("The mean square error is" , (mean_squared_error(y_test,predeicted_output,multioutput='raw_values')))
            except (RuntimeError, TypeError, NameError) as e:
                st.error('Select your features or check your parameters')
                st.write(e)
                st.stop()




    def decisionTreeClassifier(features,labels,params,X_train,X_test,y_train,y_test):
        with st.container():
            with st.form('decision tree'):
                if st.form_submit_button('Submit Decision Tree Parameters',help='Click this button to send your selected parameters to the model'):
                    st.success("Parameter Submitted Succesfully")
            try:
                if st.checkbox("Build"):
                    #st.dataframe(params)
                    with st.spinner(text='Wait while your model is been buid...'):
                        time.sleep(3)
                    st.success('Done')
                    dtc = DecisionTreeClassifier(splitter=params['splitter'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
                    min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'],max_leaf_nodes=params['max_leaf_nodes'])
                    clf = dtc.fit(X_train,y_train)
                    predeicted_output = clf.predict(X_test)
                    st.header('The Predicted plants are')
                    st.dataframe(predeicted_output)
                    st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output,normalize=False)*100))
                    model_name = f'{columns[0]}-{columns[1]}-{columns[2]}-{columns[3]}-'
                    if st.button('Save Model'):
                        try:
                            saveModel(model=clf,model_name=model_name)
                            st.success('Model saved')
                        except Exception as e:
                            st.error('Error is saving model')
            except (RuntimeError, TypeError, NameError) as e:
                st.warning("Select your features or check your parameters")
                st.stop()
            






    def knearstNeighborClassifier(features,labels,params,X_train,X_test,y_train,y_test):
        with st.container():
            with st.form('knearest '):
                if st.form_submit_button('Submit Nearest Neighbor Parameters',help='Click this button to send your selected parameters to the model'):
                    st.success("Parameter Submitted Succesfully")
            try:
                if st.checkbox("Build"):
                    #st.write(params)
                    with st.spinner(text='Wait while your model is been buid...'):
                        time.sleep(3)
                    st.success('Done')
                    knn = KNeighborsClassifier(n_neighbors=params['n_neighbors'],weights=params['weights'],algorithm=params['algorithm'],leaf_size=params['leaf_size'])
                    clf = knn.fit(X_train,y_train)
                    predeicted_output = clf.predict(X_test)
                    st.header('The Predicted plants are')
                    st.dataframe(predeicted_output)
                    st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))
                    model_name = f'{columns[0]}-{columns[1]}-{columns[2]}-{columns[3]}-'
                    if st.button('Save Model'):
                        try:
                            saveModel(model=clf,model_name=model_name)
                            st.success('Model saved')
                        except Exception as e:
                            st.error('Error is saving model')
            except:
                st.error('Select your features or check your parameters')
                st.stop()






    def supportVectorMachine(features,labels,params,X_train,X_test,y_train,y_test):
       with st.container():
            with st.form('svm '):
                if st.form_submit_button('Submit Support Vector Parameters',help='Click this button to send your selected parameters to the model'):
                    st.success("Parameter Submitted Succesfully")
            try:
                if st.checkbox("Build"):
                    #st.write(params)
                    with st.spinner(text='Wait while your model is been buid...'):
                        time.sleep(3)
                    st.success('Done')
                    svm = SVC(C=params['C'],kernel=params['kernel'],gamma=params['gamma'],verbose=params['verbose'],random_state=params['random_state'])
                    clf = svm.fit(X_train,y_train)
                    predeicted_output = clf.predict(X_test)
                    st.header('The Predicted plants are')
                    st.dataframe(predeicted_output)
                    st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))
                    model_name = f'{columns[0]}-{columns[1]}-{columns[2]}-{columns[3]}-'
                    if st.button('Save Model'):
                        try:
                            saveModel(model=clf,model_name=model_name)
                            st.success('Model saved')
                        except Exception as e:
                            st.error('Error is saving model')
            except:
                st.error('Select your features or check your parameters')
                st.stop()
