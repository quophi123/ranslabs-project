import streamlit as st 
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

class Buildmodel:


    def build(self):
        list_of_models = ['RandomForest','DecisionTree','KNearestNeibhor','SupportVectorMachine']
        algorithm=st.sidebar.selectbox('select your prefered algorithm',list_of_models)

        if algorithm == "RandomForest":
            output = 'Random Forest Here'
        elif algorithm == "DecisionTree":
            output ='DecisionTree Here'
        elif algorithm == "KNearestNeibhor":
            output ='DecisionTree Here'
        elif algorithm == "SupportVectorMachine":
            output ='SupportVectorMachine Here'
        return st.write(output)







#models function

def SupportVectorMachine(data):
    svm = SVC()
    pass



def RandomForest(data):
    rdm = RandomForestClassifier()
    pass



def DecisionTree(data):
    tree = DecisionTreeClassifier()
    pass



def KNearestNeibhor(data):
    knn = KNeighborsClassifier()
    pass

