#Load libraries needed
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_lottie import st_lottie
from sklearn.linear_model import LinearRegression


#define app section
header=st.container()
prediction=st.container()

# Define the Lottie animation URL
lottie_animation_url = "https://lottie.host/89f1f8df-aa47-4771-9441-91da251470e2/qGrHDGTqFH.json"

#define header
with header:
    header.title("Sales Prediction App With Linear Regression Across Favorita Stores")

    # Display the Lottie animation using st_lottie
    st_lottie(lottie_animation_url,height=200)

    
    header.write("On this page,you can predict sales")

