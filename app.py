import streamlit as st
from predict import show_predict_page 
from explore_page import show_explore_page


selection=st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))
if selection=="Predict":show_predict_page()
else:show_explore_page()
