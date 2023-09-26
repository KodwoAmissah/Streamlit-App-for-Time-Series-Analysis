##import libraries
import streamlit as st
import pandas as pd
import numpy as np

##define functions
@st.cache_resource()
def load_data(path):
    dataset=pd.read_csv("Notebook\\train_data.csv")
    return dataset

#load the dataset
r_path="Notebook\\train_data.csv"
load_df=load_data(r_path)

#Define section
data=st.container()

##set up data section tht users will interact with
with data:
    data.write("On this page,you can preview the dataset")

    if data.button("Preview the dataset"):
        data.write(load_df)