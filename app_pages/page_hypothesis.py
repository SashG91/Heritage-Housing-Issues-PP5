'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

def page_hypothesis():

    st.success(
        f"### Project Hypothesis and Approval\n\n"
        f"* The following are the hypotheses that I have made for this project: "
        f" The need to evaluate other houses in the area of Ames, Iowa, based on similar attributes"
        f" of the clients 4 inherited houses will give us a"
        f"prediction of sales price for each house respectively\n\n"

        f"* 1. I assume that the ground floor "
        f"living area, first floor, basement and the garage, play a "
        f"key role in determining the sale price.\n"
        f"* 2. The year the house was built and the overall quality "
        f"of materials used (finishes) in the house also play a "
        f"significant role in determining houses sales price.\n"
    )