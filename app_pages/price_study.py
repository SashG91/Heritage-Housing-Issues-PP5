'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

from src.file_management import load_housing_price_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def page_sale_price_study_body():

    # load data
    df = load_housing_price_data()

    # hard copied from sale price study notebook
    # The 5 variables that correlate to Sale Price
    # These variables will be tested on strength to predicting Sale Price
    corr_var_list = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### House Sale Price Study")
    st.info(
        f"* The client is interested in discovering how the house attributes "
        f"correlate with the sale price.\n"
        f"* Therefore, the client expects data visualizations of the "
        f"correlated variables against the sale price to show that."
        )