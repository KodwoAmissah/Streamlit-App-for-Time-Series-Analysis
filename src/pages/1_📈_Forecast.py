#Load libraries needed
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_lottie import st_lottie
from datetime import datetime


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


# Create lists
inputs = ["date", "holiday", "locale", "transferred", "onpromotion"]
categorical = ["holiday", "locale", "transferred"]


# Set up prediction container
with st.expander("Make a prediction", expanded=True):

   # Define our inputs
    date = st.date_input(label="Enter a date")

    holiday = st.selectbox(label="Select a category of holiday", options=['Holiday', 'Not Holiday', 'Work Day', 'Additional', 'Event', 'Transfer', 'Bridge'])
    locale = st.radio(label="Select a holiday type", options=['National', 'Not Holiday', 'Local', 'Regional'], horizontal=True)
    transferred = st.radio(label="Select whether the holiday was transferred or not", options=["True", "False"], horizontal=True)
    onpromotion = st.number_input(label="Please enter the total number of expected items to be on promotions")

    # Create a button
    predicted = st.button("Predict")

    
    # Upon predicting
    if predicted:
        # Format for inputs
        input_dict = {
        "date":[date],
        "holiday": ["holiday"],
        "locale": [locale],
        "transferred": [transferred],
        "onpromotion": [onpromotion]
            
        }

        # Convert inputs into a DataFrame
        input_df = pd.DataFrame.from_dict(input_dict)

        #create a copy that will make output understandable
        predict_df=input_df.copy()
      
       # Load the encoders from files
        LE = joblib.load('Encoders\\label_encoder.pkl')
        BE = joblib.load('Encoders\\binary_encoder.pkl')
        OE = joblib.load('Encoders\\ordinal_encoder.pkl')

        # Encode categorical inputs
        input_df["transferred"] = LE.transform(input_df["transferred"])
        input_df= BE.transform(input_df)
        input_df["locale"]=  OE.transform(input_df[["locale"]]) 
           
         #Convert date to datetime
        input_df["date"] = pd.to_datetime(input_df["date"])
       
        # Extract date features and add to input_df
        input_df['year'] = input_df['date'].dt.year
        input_df['month'] = input_df['date'].dt.month
        input_df['day'] = input_df['date'].dt.day
        input_df['day_of_week'] = input_df['date'].dt.dayofweek
        input_df['day_of_year'] = input_df['date'].dt.dayofyear
        input_df['week_of_year'] = input_df['date'].dt.isocalendar().week
        input_df['quarter'] = input_df['date'].dt.quarter
        input_df['is_weekend'] = (input_df['date'].dt.dayofweek // 5 == 1).astype(int)
        input_df['day_of_month'] = input_df['date'].dt.day

        ##we drop date after extracting
        input_df.drop(columns=['date'], inplace=True)
        
         # Load the model
        model = joblib.load('Model\\model.pkl')

        # Make predictions
        model_output = model.predict(input_df)

        # Add predictions to the input DataFrame
        predict_df["Total Sales"] = model_output

        # Display predictions
        st.write("Forecast output")
        st.dataframe(predict_df)
        