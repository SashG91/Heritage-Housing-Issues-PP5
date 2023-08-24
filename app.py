'''
Following content is taken from the Churnometer 
Walkthrough Project 2 and adapted for this project.
'''

import streamlit as st

from app_pages.page_multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary
from app_pages.page_predict_sales_price import page_price_study
from app_pages.page_price_predictor import page_price_predictor
from app_pages.page_hypothesis import page_hypothesis
from app_pages.page_predict_sales_price import page_predict_sales_price

# Create an instance of the app
app = MultiPage(app_name="House Price Predictor")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary)
app.add_page("House Sale Price Study", page_sale_price_study)
app.add_page("Price Predictor", page_price_predictor)
app.add_page("Project Hypothesis", page_project_hypothesis)
app.add_page("ML: House Sale Price Prediction", page_predict_sale_price)

app.run()  # Run the app