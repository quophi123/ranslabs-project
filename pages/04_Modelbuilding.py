from pytz import NonExistentTimeError
import streamlit as st 
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
from sklearn.model_selection import train_test_split


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



#models function
def supportVectorMachine():
    params = dict()
    C = st.slider("C",min_value=0,max_value=10)
    params.update({"C":C})
    random_state = st.slider("random_state",1,5)
    params.update({"random_state":random_state})
    kernel = st.radio("kernel",('rbf','poly', 'linear','sigmoid','precoumputed'))
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
    n_estimators = st.slider("Select Number of estimators",min_value=0,max_value=100)
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
    max_leaf_nodes = st.slider("max_leaf_nodes",min_value=None,max_value=10)
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

features = ...
labels = ...

#X_train,X_test,y_train,y_test = train_test_split(features,labels, test_size=test_size)




if algorithm == "RandomForest":
    
    with st.form('random forest'):
        params = randomForest()
        submit = st.form_submit_button('Submit Random Forest Parameters')
    if submit:
        st.write(params)
        rdm = RandomForestClassifier(n_estimators=params['n_estimators'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
        min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'])
        



elif algorithm == "DecisionTree":
    with st.form('decision tree'):
        params = decisionTree()
        submit = st.form_submit_button('Submit Decision Tree Parameters')
    if submit:
        st.write(params)
        dtc = DecisionTreeClassifier(splitter=params['splitter'],max_depth=params['max_depth'],min_samples_split=params['min_samples_split'],
        min_samples_leaf=params['min_samples_leaf'],max_features=params['max_features'],random_state=params['random_state'],max_leaf_nodes=params['max_leaf_nodes'])
        




elif algorithm == "KNearestNeibhor":
    with st.form('knearest '):
        params = kNearestNeibhor()
        submit = st.form_submit_button('Submit Nearest Neighbor Parameters')
    if submit:
        st.write(params)
        knn = KNeighborsClassifier(n_neighbors=params['n_neighbors'],weights=params['weights'],algorithm=params['algorithm'],leaf_size=params['leaf_size'])





elif algorithm == "SupportVectorMachine":
    with st.form('svm '):
        params = supportVectorMachine()
        submit = st.form_submit_button('Submit Support Vector Parameters')
    if submit:
        st.write(params)
        svm = SVC(C=params['C'],kernel=params['kernel'],gamma=params['gamma'],verbose=params['verbose'],random_state=params['random_state'])




