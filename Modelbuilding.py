from pytz import NonExistentTimeError
import streamlit as st 
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split




#models function


# SVC parameters function
def supportVectorMachine():
    params = dict()
    C = st.slider("C",min_value=0,max_value=10)
    params.update({"C":C})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    kernel = st.radio("kernel",('rbf','poly', 'linear','sigmoid','precoumputed'))
    params.update({"kernel":kernel})
    gamma = st.radio("gamma",('scale','auto'))
    params.update({"gamma":gamma})
    verbose = st.radio("verbose",(True,False))
    params.update({"verbose":verbose})
    
    return params
    pass






#Randomforest parameters functions
def randomForest():  
    params = dict()
    n_estimators = st.slider("Select Number of estimators",min_value=0,max_value=100)
    params.update({"n_estimators":n_estimators})
    max_depth = st.slider("Select maximum dept",10)
    params.update({"max_depth":max_depth})
    min_samples_split = st.slider("minimun sample split",2,10)
    params.update({"min_samples_split":min_samples_split})
    min_samples_leaf = st.slider("min_samples_leaf",1,10)
    params.update({"min_samples_leaf":min_samples_leaf})
    max_features = st.radio("max_features",('sqrt','log', 'None'))
    params.update({"max_features":max_features})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    st.write(params['n_estimators'])
    return params




#Decisiontree parameters function
def decisionTree():
    tree = DecisionTreeClassifier()
    params = dict()
    splitter = st.radio("splitter",('best','random'))
    params.update({"splitter":splitter})
    max_depth = st.slider("Select maximum dept",10)
    params.update({"max_depth":max_depth})
    min_samples_split = st.slider("minimun sample split",2,10)
    params.update({"min_samples_split":min_samples_split})
    min_samples_leaf = st.slider("min_samples_leaf",1,10)
    params.update({"min_samples_leaf":min_samples_leaf})
    max_features = st.radio("max_features",('auto','sqrt','log', 'None'))
    params.update({"max_features":max_features})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    max_leaf_nodes = st.slider("max_leaf_nodes",min_value=None,max_value=10)
    params.update({"max_leaf_nodes":max_leaf_nodes})
    return params
    pass




#Kneighbors parameters
def kNearestNeibhor():
    knn = KNeighborsClassifier()
    params = dict()
    n_neighbors = st.slider("n_neighbors",min_value=3,max_value=10)
    params.update({"n_neighbors":n_neighbors})
    weights = st.slider("weights",('uniform','distance'))
    params.update({"weights":weights})
    algorithm = st.slider("algorithm",('auto','ball_tree','kd_tree','brute'))
    params.update({"algorithm":algorithm})
    leaf_size = st.slider("leaf_size",30,100)
    params.update({"leaf_size":leaf_size})
    return params
    pass






















class Buildmodel:


    def build(self):
        list_of_models = ['RandomForest','DecisionTree','KNearestNeibhor','SupportVectorMachine']
        algorithm=st.sidebar.selectbox('select your prefered algorithm',list_of_models)

        test_size = st.slider('Select the size of your test data',(10.0/100),(50.0/100),step=.05)

        features = ...
        labels = ...

        #X_train,X_test,y_train,y_test = train_test_split(features,labels, test_size=test_size)


        if algorithm == "RandomForest":
            params = randomForest()
            rdm = RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
            min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'])
            output = 'Random Forest Here'



        elif algorithm == "DecisionTree":
            params = decisionTree()
            dtc = DecisionTreeClassifier(splitter=params['splitter'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
            min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'],max_leaf_nodes=params['max_leaf_nodes'])
           
            output ='DecisionTree Here'




        elif algorithm == "KNearestNeibhor":
            params = kNearestNeibhor()
            knn = KNeighborsClassifier(n_neighbors=params['n_neighbors'],weights=params['weights'],algorithm=params['algorithm'],leaf_size=params['leaf_size'])
           
            output ='DecisionTree Here'





        elif algorithm == "SupportVectorMachine":
            params = supportVectorMachine()
            rdm = SVC(C=params['C'],kernel=params['kernel'],gamma=params['gamma'],verbose=params['verbose'],random_state=params['random_state'])
           
            output ='SupportVectorMachine Here'




        return st.write(output)







