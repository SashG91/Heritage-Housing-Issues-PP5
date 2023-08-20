'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st
import pandas as pd
from src.file_management import load_clean_data, load_pkl_file
from src.predictive_analysis_ui import predict_sale_price

def page_price_predictor_body():

    # load predict sale price files
    ver = 'v2'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"

    price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    price_features = (pd.read_csv(f"{path}/X_train.csv")
                      .columns
                      .to_list()
                      )
    feature_importance = list(pd.read_csv(f"{path}/feature_importance.csv")['Feature'])

    st.write("### Sale Price Prediction Interface")
    st.info(
        f"* The client would like to predict the house sales price"
        f" for her 4 inherited houses, and any other house in Ames, Iowa."
        )
    st.write("---")

    st.write("### Inherited houses price prediction")
    st.info(
        f"* Below we can find the details of the inherited "
        f"houses and their individual price predictions."
        )
    total_price = predict_inherited_house_price(price_pipe, price_features)
    total_price = "%.2f" % total_price
    st.info(
        f"The sum total sale price for all your "
        f"properties is \u20AC{total_price}"
        )
    st.write("---")

    # Live Data Production
    check_var = False
    if check_var:
        check_variables_for_UI(price_features)

    st.write("### Houses Price Predictor")
    st.info(
        f"* Input the values of a property that "
        f" you wish to make a **price prediction**."
        )
    X_live = DrawInputsWidgets()

    # Live Data Prediction
    if st.button("Run Predictive Analysis"):
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              price_pipe)
        # logic for displaying the targetted sale price
        statement = (
            f"The predicted selling price for this house "
            f"is \u20AC{price_prediction}"
            )

        st.info(statement)


def predict_inherited_house_price(price_pipe, price_features):
    inherited = load_clean_data("inherited")
    row_count = len(inherited)
    inherited.index = range(1, row_count+1)
    total_price = 0
    for x in range(row_count):
        X_live = inherited.iloc[[x]]
        st.write(X_live)
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              price_pipe)
        price_prediction = "%.2f" % price_prediction
        statement = (
            f"* Predicted selling price for targetted house "
            f"{x+1} is \u20AC{price_prediction}"
            )
        total_price += float(price_prediction)
        st.write(statement)
        
    return total_price

def check_variables_for_UI(price_features):
    import itertools

