import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

titanic_data = pd.read_csv('train.csv')
def show_explore_page():
    sns.set_style("white")
    sns.color_palette("rocket", as_cmap=True)
    fig, ax = plt.subplots()
    ax=sns.countplot('Sex', hue='Survived', data=titanic_data,palette="rocket")
    st.write("""### Number of survivors gender wise ###""")
    st.pyplot(fig)
    
    fig2,ax2=plt.subplots()
    ax2=sns.countplot('Pclass', hue='Survived', data=titanic_data,palette="rocket")
    st.write("""### Number of survivors ticket class wise ###""")
    st.pyplot(fig2)
    
    
