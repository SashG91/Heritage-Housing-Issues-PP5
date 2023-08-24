'''
Following content is taken from the Churnometer 
Walkthrough Project 2 and adapted for this project.
'''
import streamlit as st
import pandas as pd
import joblib

@st.cache_data
def load_housing_price_data():
    path = "inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/"
    file = "house_prices_records.csv"
    df = pd.read_csv(path + file)
    return df

@st.cache_data
def load_clean_data(dataset):
    if dataset=="inherited":
        df = pd.read_csv("outputs/datasets/cleaned/clean_inherited_houses.csv")
    else:
        df = pd.read_csv("outputs/datasets/cleaned/clean_house_price_records.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)