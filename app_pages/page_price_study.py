'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

from src.manage_files import load_housing_price_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

def page_price_study():

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
        f"* Thus, the client expects data visualizations of the "
        f"correlated variables against the sale price to confirm."
        )
    
    # inspect data
    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"the first 10 rows are displayed below.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* Using the Pearson and Spearman methods a correlation study was undertaken "
        f"to better understand how the identified variables correlate to house sale prices.\n"
        f"* The most correlated variables extrapolated were: \n"
        f"  * **1stFlrSF, GarageArea, GrLivArea, OverallQual, TotalBsmtSF, YearBuilt**"
    )

    # Derived from the "sale price study" notebook
    st.info(
        f"#### The correlations and plots converge.\n"
        f"* The following are the variables isolated in the"
        f" correlation study:\n"
        f"* 1stFlrSF: First Floor square feet\n"
        f"* GrLivArea: Above grade (ground) living area square feet\n"
        f"* OverallQual: Rates the overall material and finish of the house\n"
        f"* TotalBsmtSF: Total square feet of basement area\n"
        f"* GarageArea: Size of garage in square feet\n"
        f"* YearBuilt: Original construction date\n\n"
        f"* The plots show that the variables, isolated in the"
        f" correlation study, do show a strong correlation and hence"
        f" possibly a strong predictive power for sale price\n"
    )

    # "EDA on the Correlated Variable List" section
    df_eda = df.filter(corr_var_list + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable correlation Sale Price"):
        variable_correlation_to_sale_price(df_eda, corr_var_list)


def variable_correlation_to_sale_price(df_eda, corr_var_list):
    # function based on the "sale price study" notebook
    # "Visualize correlation to Sale Price" section
    target_var = 'SalePrice'
    for col in corr_var_list:
        plot_numerical(df_eda, col, target_var)
        st.write("\n\n")


def plot_numerical(df, col, target_var):
    # function based on "sale price study" notebook
    # "Visualize correlation to Sale Price" section

    fig, axes = plt.subplots(figsize=(15, 8))
    sns.regplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()