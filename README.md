# **House-Price-Predictor**
<img width="1005" alt="Screenshot 2023-08-30 at 10 14 56" src="https://github.com/SashG91/Heritage-Housing-Issues-PP5/assets/97494070/ba6c795b-de92-4ebe-aff6-795ee6a84aec">

The goal for this project was to demonstrate both Machine Learning and Deep Learning concepts with respect to predicting the potential sales prices of homes using historical sale data for homes in Ames, Iowa using a dataset sourced from kaggle.com

## **Table of Contents**
XXX

## **Introduction**
This is the final project requirement for my Code Institute Full Stack Developer program. The project aims at targeting topics of Python applications, Deep Learning, Machine Learning, business case analysis, API integration and dashboard generation through the use of Streamlit.

Link to the project dashboard is [here](https://sash-heritage-housing-issues-68817101fc6d.herokuapp.com/).

## **Business Requirements**

The client Lydia Doe, has inherited four properties from a family member and they are located in Ames, Iowa, She has thus requested us to help in predicting the selling price of the properties should she wish to put them on the market. Due to Lydia's limited knowledge of the local housing market she is worried about skewed pricing estimations which will result in losing more if she sells.. Thus, she seeks the expertise of a data practitioner to predict the sales price of the inherited properties and any other residential properties in Ames, Iowa. We therefore put forward the following client requests:

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. There is an expectation for data visualisations of the correlated variables against the sale price to cofirm.
  
* 2 - The client would like to predict the house sale price of the four inherited houses including any other residential properties in Ames, Iowa.

To fulfill the clients expectations, we will build an Application (Dashboard) that predicts the sales price of the four inherited houses based on their attributes. The dashboard interface will give Lydia an opportunity to explore how the house attributes correlate with the sale price using data visualizations.
  
## **Dataset Content**

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
* We then created user stories where predictive analytics can be applied in a workplace. 
* The dataset consists of almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profiles made up of, but not limited to (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## **Hypotheses for Case Study**
The following are the hypotheses that I have made for this project:

1. I assume that a house with a greater GrLivArea sells for a higher price. We could possible confirm this with a linear correlation analysis between OverallQual and SalePrice.

2. I also put forward that the YearBuilt date and the OverallQual of materials (finishes) affects the sales price.  We could possible confirm this with a correlation analysis between YearBuilt and SalePrice can show this relationship.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

**Business Requirement 1:** 
Data Visualization and Correlation.

* We will examine the housing price statistics from the public dataset.
* We will conduct a correlation and/or PPS study to investigate the most suitable variables correlating to the sale price.
* We will present and summarize the data after visualizing these variables vs the sale price.

**Business Requirement 2:** 
Regression and Data Analysis.

* We will provide a ML algorithm that can accurately forecast the combined sales price of the four inherited houses.
* We will map the relationships between the characteristics and the target using conventional ML.
* Regression will be used to estimate the connection between the variables and the target.
* Develop a dashboard that allows Lydia to explore how the house attributes correlated with the sale price using data visualizations.

<h2>The CRISP-DM (Cross Industry Standard Process for Data Mining)</h2>
The flow and structure were combined with the Cross Industry Standard Process for Data Mining also known as Crisp-DM.
CRISP-DM is a modelled process that builds the foundation for a data science process. It has to progress through six phases in the below order:

* What does the business need in terms of business understanding?
* Understanding data: What information do we have or need? How clean is it?
* Data organization - How should the data be set up for modeling?
* Modeling - Which modeling approaches should we use?
* Evaluation: Which model best satisfies the business's goals?
* Deployment - How can stakeholders have access to the results, via an API or Dashboard?

  ### **User Stories - Client**

1. As a client, I want to see a set of visualizations that show the correlated variables against the sale price so that I can better understand the relationship between the features and the price.

2. As a client, I want to be able to input most desirable features of a house and get an accurate prediction of the sale price so that I can make informed decisions about buying or selling properties in Ames, Iowa.

3. As a client, I want to be able to see the predicted sale price of all inherited properties so that I can make informed decisions when deciding to sell them.

4. As a client, I want a data application that is user-friendly and easy to use so that I can quickly and easily access the information I need to make informed decisions.

### **User Stories - Data Practitioner**
From the project requirements, we can create a list of user stories for either a data practioner or standard non-technical user.

1. As a data practitioner, I want to import a public dataset into the system so that I can build a model to predict the sales price of the inherited houses located in Ames, Iowa.

2. As a data practitioner, I want to clean and process the dataset so that I can build an accurate model for predicting house prices.

3. As a data practitioner, I want to explore the dataset to understand the features and their relationships with the sale price so that I can create valuable visualizations.

4. As a data practitioner, I want to build a predictive model that accurately predicts the sale price of the inherited properties as well as any other house in Ames, Iowa.

5. As a data practitioner, I want to optimize the model's hyperparameters to ensure that it is as accurate as possible to the clients expected requirements.

6. As a data practitioner, I want to test the model's efficiency and accuracy and ensure that it is reliable for achieving our needs.

## ML Business Case
#### Predict House Prices in Ames, Iowa

**Regression model**

* We are looking for a machine learning model that can help forecast the house prices in Ames, Iowa. Our client may utilize the model to make the best decision in terms of selling the four inherited residences. Our target variable is numerical and contains the expected house price depending on the features chosen form the dataset that may influence sales prices the most. We take into account a supervised, one-dimensional regression model.
* Our desired result is to provide our client with trustworthy information so that our client can feel confident when making informed decisions for the homes and potentially and future homes in Ames, Iowa.
  
  * The model success metrics are:
* At least 0.7 for R2 score, on the train and test set (results can be found in Summary Section below).
* The ML model is considered a failure if the model is wrong by more than 30% after 12 months, the prediction need to be consistent over a long period of time.
* The output is defined as a numerical value for price in dollars. The prediction is made on the fly (not in batches).

## **Dashboard Design**

This section introduces the use of the Streamlit dashboard APP that would be delivered to the client as requested.

## **Wireframes**
XXX

### **Running the application**
The streamlit app/dashboard is delpoyed through heroku, as discussed step-by-step in the deployment section below.

If you wish to run the the app locally prior to deployment we can run the following command in the terminal:

    streamlit run app.py

This will run a local version of the app on your machine.

Below shows the breakdown of the final streamlit app according to each page:

<h3>Page 1: Quick Project Summary</h3>
A high-level summary of the project, including:

* Information on the dataset
* The business and client (Lydia Doe's) requirements.
* Dataset guidelines.

<h3>Page 2: House Sale Price Study</h3>
A page that displays the relationships between pricing and features.
* Inspection of house price data in table format (snapshot)
* Lists the most suitable features to be used from the dataset.
* Shows the correlation of targetted features and sales price.
* A series of plots showing the relationship between each feature and sales price.

### **Answers Business Requirement 1**

* We will inspect the data related to house prices.
* To analyze the factors most likely to be connected with the sale price, we shall conduct a correlation research.
* These variables will be compared to the sale price, and the insights will be shown and summarized.

<h3>Page 3: Predict House Sale Price</h3>
On this page the client may forecast the price of her inherited houses as well as the sale price of any house in Ames, Iowa.
* Provides the details of each inherited house individually and their expected sale price.
* A summed value should all 4 inherited houses be sold.
* Provides an House Price Predictor interface where a user can input 1stFlr | GrLivArea | GarageArea | YearBuilt in order to run a Predictive Analysis so as to determine the expected sale price of a house.

### **Answers Business Requirement 2**
  
* Widgets to predict a house sale price based on the selected features.
* Display estimated sale price on the inherite houses of the client and give a total sum of all 4 inherited houses.

<h3>Page 4: Project Hypothesis and Validation</h3>
This page answers the hypothesis we had before we started the project.

1. The first hypothesis is that a house with a greater GrLivArea sells for a higher price. In our study of house prices, we discovered that there was a significant association using both the pearson and spearman methodologies, supporting the hypothesis.

2. The second hypothesis is that the YearBuilt date and the overall quality of materials (finishes) affects the sales price. After our study, we saw a weak link between these qualities; nevertheless, there is no clear data to support this.

<h3>Page 5: ML: House Sale Price Prediction </h3>
This page contains information about the ml pipeline.

* Shows the ML Pipeline used.
* Displays the best features the model was trained on.
* Shows Performance and evaluation by confirming the clients R2 score and validated with the produced R2 score.

## **Unfixed Bugs**
* No bugs of note.

## **Conclusion**
### **Summary of Findings**
Below we can confirm if we have satisfied all business requirements:

|Business Requirement|Satisfied?|
|:---|:---|
|Perform a correlation study to investigate the most relevant variables correlated to the sale price.| :white_check_mark: |
|Produce an ML system that can predict the summed sale price of four inherited properties, as well as any other house in Ames, Iowa.| :white_check_mark: |
|Deliver either a conventional ML or Neural network based system.| :white_check_mark: |
|Develop a dashboard that allows our client to explore how the house attributes correlated with the sale price through data visualizations.| :white_check_mark: |
|Consider changing from regression to classification if dataset if variables allow for it.| :white_check_mark: |
|Perform an extensive hyperparameter search for a given algorithm.| :white_check_mark: |

* We can predict the prices of other houses in Ames, Iowa if desired.
* We can predict the total sum of selling all four inherrited houses: $650399.59
* We have satisfied all business requirements proposed for this case study.
* We achieved an R2 score of 0.97 on the train set and 0.78 on the test set.

  ## **Results**
Using the final pipeline, the inherrited house records were introduced to so as to yield the following results:

|House|OverallQual|GarageArea|GrLivArea|YearBuilt|Sale Price|
|:----|:----|:----|:----|:----|:----|
|1|5|730|896|1961|$130132.30|
|2|6|312|1329|1958|$153067.17|
|3|5|482|1629|1997|$186517.88|
|4|6|470|1604|1998|$180682.24|
|||||Total Sum|$650399.59|

## **Deployment**
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version 3.10.11
* The project was deployed to Heroku using the following steps.
1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## **Main Data Analysis and Machine Learning Libraries**
1. [Heroku](https://dashboard.heroku.com/apps)
    * Used to host the project for the clients dashboard.
2. [pyenv](https://github.com/pyenv/pyenv)
    * Used to manage the multiple versions of python installed on my local machine and set the required python version for the virtual environment.
4. [scikit learn](https://scikit-learn.org/stable/)
    * Used to implement core ML functions.
5. [Feature Engine](https://feature-engine.trainindata.com/en/latest/index.html)
    * Used for to facilitate core feature engineering and selection functions.

## **Credits and Acknowledgements**
1. Code Institute Data Analytics programme, guidance from the Walkthrough Project 2-Churnometer.
2. The provided repository template found [here](https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues) was used for this project.
3. The data source for this project is located [here](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)
4. Stack overflow for guidance on converting a single dataframe.
5. My mentor Alex Konovalov for his patience and expertise during the process and every mentor meeting.
6. Code institute peer Adam Boley for setting me on the correct track with timelines and always checking in to see if i've made steady progress.
