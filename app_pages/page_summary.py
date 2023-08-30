'''
This file and its contents have been informed and adapted 
from the Churnometer Walkthrough Project 2.
'''

import streamlit as st

def page_summary():

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
        f"* For additional information, please refer to this link below for the project Readme"
        f"*[Project README file](https://github.com/SashG91/Heritage-Housing-Issues-PP5/blob/main/README.md)"
        )
    
    st.info(
        f"**Dataset Content Guidelines**\n\n"
        f"|Variable|Meaning|Units|\n"
        f"|:----|:----|:----|\n"
        f"|1stFlrSF|First Floor square feet|334 - 4692|\n"
        f"|2ndFlrSF|Second floor square feet|0 - 2065|\n"
        f"|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|\n"
        f"|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|\n"
        f"|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|\n"
        f"|BsmtFinSF1|Type 1 finished square feet|0 - 5644|\n"
        f"|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|\n"
        f"|TotalBsmtSF|Total square feet of basement area|0 - 6110|\n"
        f"|GarageArea|Size of garage in square feet|0 - 1418|\n"
        f"|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        f"|GarageYrBlt|Year garage was built|1900 - 2010|\n"
        f"|GrLivArea|Above grade (ground) living area square feet|334 - 5642|\n"
        f"|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|\n"
        f"|LotArea| Lot size in square feet|1300 - 215245|\n"
        f"|LotFrontage| Linear feet of street connected to property|21 - 313|\n"
        f"|MasVnrArea|Masonry veneer area in square feet|0 - 1600|\n"
        f"|EnclosedPorch|Enclosed porch area in square feet|0 - 286|\n"
        f"|OpenPorchSF|Open porch area in square feet|0 - 547|\n"
        f"|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        f"|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        f"|WoodDeckSF|Wood deck area in square feet|0 - 736|\n"
        f"|YearBuilt|Original construction date|1872 - 2010|\n"
        f"|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|\n"
        f"|SalePrice|Sale Price|34900 - 755000|\n"
        )    

      

