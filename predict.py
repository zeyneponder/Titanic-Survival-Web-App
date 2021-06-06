import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl',"rb")as file:
        data=pickle.load(file)
    return data

data=load_model()
regressor=data["model"]

Sex=0
Embarked=0
def show_predict_page():
    st.title("Titanic Survival Prediction")
    Sx=[
        "Male",
        "Female"
    ]
    Clss=[1,2,3]
    Location=["Cherbourg","Queenstown","Southampton"]
    
    Sex_st=st.selectbox("Select your sex:",Sx)
    Age=st.slider("Select your age:",0,60,1)
    Class=st.selectbox("Preferred ticket class?",Clss)
    Fare=st.slider("Ticket fare in $:",0,500,50)
    Embarked_st=st.selectbox("Embark Location:",Location)
    
    if Sex_st=="Male":Sex=0
    else: Sex=1
   
    if (Embarked_st=="Southampton"):Embarked==0
    elif (Embarked_st=="Cherbourg"):Embarked==1
    else:Embarked==2
        
    ok=st.button("See if you could survive")
    
    if ok:
        x=[[Class,Sex,Age,0.5,0.4,Fare,Embarked]]
        
        survival=regressor.predict(x)
        if survival[0]==0:st.write("Unfortunately, you probably could not survive.")
        elif survival[0]==1:st.write("You are lucky, you probably could survive.")
