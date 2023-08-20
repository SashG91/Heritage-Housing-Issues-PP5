'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The project dataset was sourced from **[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)**.\n"
        f"* The full dataset consisted of almost 1.5 thousand rows and represents housing records from Ames, Iowa. "
        f"The dataset typically represents multiple house profiles or aspects of a property "
        f"ie. Year built, Floor Areas, Garage, Basement, Kitchen, Lot, Porch "
        f"and the respective sale price, for houses that were built between years 1872 and 2010.")

    # "Business Requirements" section
    st.success(
        f"The client presented 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how house attributes correlate with potential sale price.\n"
        f"  * The client is expecting data visualizations of the correlated variables against the sale price.\n"
        f"* 2 - The client would also like to establish the house sales price of 4 inherited houses "
        f"and any other house in Ames, Iowa."
        )

    # README file, for full project documentation
    st.info(
        f"* For additional information, please refer to this link for the project Readme"
        f"[INSERT README URL HERE"
        )
    
    

      

