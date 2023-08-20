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