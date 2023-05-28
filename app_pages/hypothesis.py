'''
This file and its contents has been informed and adapted 
from the Churnometer Walkthrough Project.
'''

import streamlit as st

def hypothesis_body():

    st.info(
        "### Project Hypothesis\n\n"
        "The following are the hypotheses that I put forward for this project:\n\n"
        "1. I assume that a house with greater OverallQual would sell for a higher price.\n"
        "We could possible confirm this with a correlation analysis between OverallQual and SalePrice.\n\n"
        "2. I further assume that a house with a bigger garage sells for a higher price.\n"
        "We could possible confirm this with a correlation analysis between GarageArea and SalePrice can show this relationship.\n\n"
    )

    # Validation of hypotheses
    st.write("---")
    st.write("### Hypothesis Validation")