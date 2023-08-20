'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.file_management import load_clean_data, load_pkl_file
from src.eval_pipeline_perf import regression_performance
from src.eval_pipeline_perf import regression_evaluation_plots

def page_predict_sale_price_body():

    # load sale price pipeline files
    ver = 'v2'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"
    sale_price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    feat_importance = pd.read_csv(f"{path}/feature_importance.csv")
    feat_importance_plot = plt.imread(f"{path}/feature_importance.png")
    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv")
    y_test = pd.read_csv(f"{path}/y_test.csv")

    st.write("### ML Pipeline: Predict House Sale Price")

    # display pipeline training summary conclusions
    st.info(
        f"* We used Linear Regressor model to predict sale price "
        f"for a single property\n"
        f"* Both feature selection and PCA produced similar results and was found to meet "
        f"business requirement 1. By a small margin, feature selection "
        f"gave better performance. Therefore, the best pipeline to use will be that "
        f"of feature selection.\n"
        f"* Feature selection achieved an R2 Score: 0.97 on the train set and "
        f"an R2 Score: 0.78 on the test set respectively.\n"
        f"* The clients requirement was for an R2 Score of 0.75\n"
        )
    st.write("---")