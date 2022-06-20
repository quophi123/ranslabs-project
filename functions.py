#import modules
import streamlit as st
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
                    height=500,allow_unsafe_jscode=True,theme='fresh')
    selected_rows = gridtable['selected_rows']
    st.header("Selected Columns")
    st.dataframe(selected_rows)









class Modelbuilding:

    def randomForestClassifier(features,labels,params,X_train,y_train,y_test):
        with st.form('random forest'):
            pass
            if st.form_submit_button('Submit Random Forest Parameters'):
                st.success("Parameter Submitted Succesfully")
        if st.button("Build"):
            st.write(params)
            rdm = RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
            min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'])
            clf = rdm.fit(X_train,y_train)
            predeicted_output = clf.predict(np.array([1.4,1.8,2,5.4]).reshape(1,-1))
            st.write(predeicted_output)
            #st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))
    




    def decisionTreeClassifier(features,labels,params,X_train,y_train,y_test):
        with st.form('decision tree'):
            pass
            if st.form_submit_button('Submit Decision Tree Parameters'):
                st.success("Parameter Submitted Succesfully")
        try:
            if st.button("Build"):
                #st.dataframe(params)
                dtc = DecisionTreeClassifier(splitter=params['splitter'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
                min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'],max_leaf_nodes=params['max_leaf_nodes'])
                clf = dtc.fit(X_train,y_train)
                predeicted_output = clf.predict(np.array([1.5,4,5.9,1.3]).reshape(1,-1))
                st.header(f"The predicted plant is : `{predeicted_output}`")
                st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output,normalize=False)*100))
        except:
            st.warning("Check Your Parameter inputs")
        






    def knearstNeighborClassifier(features,labels,params,X_train,y_train,y_test):
        with st.form('knearest '):
            pass
            if st.form_submit_button('Submit Nearest Neighbor Parameters'):
                st.success("Parameter Submitted Succesfully")
        if st.button("Build"):
            st.write(params)
            knn = KNeighborsClassifier(n_neighbors=params['n_neighbors'],weights=params['weights'],algorithm=params['algorithm'],leaf_size=params['leaf_size'])
            clf = knn.fit(X_train,y_train)
            predeicted_output = clf.predict(np.array([1.4,1.8,2,5.4]).reshape(1,-1))
            st.write(predeicted_output)
            #st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))







    def supportVectorMachine(features,labels,params,X_train,y_train,y_test):
        with st.form('svm '):
            pass
            if st.form_submit_button('Submit Support Vector Parameters'):
                st.success("Parameter Submitted Succesfully")
        if st.button("Build"):
            st.write(params)
            svm = SVC(C=params['C'],kernel=params['kernel'],gamma=params['gamma'],verbose=params['verbose'],random_state=params['random_state'])
            clf = svm.fit(X_train,y_train)
            predeicted_output = clf.predict(np.array([1.4,1.8,2,5.4]).reshape(1,-1))
            st.write(predeicted_output)
            #st.write("The accuracy score is" , (accuracy_score(y_test,predeicted_output)*100))
