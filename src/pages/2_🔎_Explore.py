##Load libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly

#load model
model=joblib.load("Model/model.pkl")

# Define functions
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset

# Load the dataset
data_path = "Dataset/train_data.csv"
load_df = load_data(data_path)

#load test data to see model's performnce
test_df=pd.read_csv("Dataset/test.csv")

# Define section
data = st.container()

# Set up the data section that users will interact with
with data:
    data.title("On this page, you can preview the dataset and view daily sales across stores")
    st.write("View the Dataset below")

    # Button to preview the dataset
    if st.button("Preview the dataset"):
        data.write(load_df)

    # Button to view the chart

    st.write("Graph showing daily sales can be viewed below")
    if st.button("View Chart"):

        # Set the "date" column as the index
        load_df = load_df.set_index('date')

        # Display the line chart with dates on the x-axis
        st.subheader("A Chart of the Daily Sales Across Favorita Stores")
        st.line_chart(load_df["sales"])

##Adding visua#lof model prediction        
st.write("View the model's prediction")
if st.button("Model's graph"):

    # we predict with the model
    result = model.predict(test_df)

    # Create a Plotly line chart for the model's predictions
    fig = px.line(x=test_df.index, y=result, title="Model's Forecast")

    # Display the chart using st.plotly_chart()
    st.subheader("A plot of model's forecast")
    st.plotly_chart(fig)

    







