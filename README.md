# Data Science Portfolio 


This repository is a portfolio of data science projects I’ve completed. Many of the projects are designed to solve real-world problems I’ve encountered in my political/advocacy career, other projects were completed for educational purposes. Python based projects are typically presented in Jupyter Notebooks, with the exception of ad hoc programs such as web scrapers built to gather data for specific projects. SQL projects will contain a read me markdown file that will walk through the project step by step. Each step will contain links to relevent SQL files. Data visualization projects will contain links to Tableau public where you can view and interact with the visualizations and dashboards.


# [Ozone Forecasting Model](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/voter_turnout_model/final_2019_denver_model.ipynb)

### **Project Overview**

At ground level, ozone is a pollutant and a component of smog. It forms through chemical reactions involving sunlight, nitrogen oxides (NOx), and volatile organic compounds (VOCs) emitted by various sources such as vehicles and industries. High levels of ground-level ozone can cause respiratory issues and worsen conditions like asthma and COPD. Monitoring ozone levels helps assess overall air pollution and the effectiveness of pollution control measures.

The goal of this project is to use time series data to build a model to forecast how much ozone will be present in the air of Los Angeles, CA. 

### Skills

- Python, Prophet, Sklearn
- Pandas, matplotlib, numpy, seaborn

# [Cycling Brand Sentiment Analysis](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/cycling_brand_sentiment)

### **Project Overview**

* Sentiment analysis is a technique used to understand and interpret people's feelings and opinions expressed in text. It helps us figure out whether a piece of text, like a review or social media post, conveys a positive, negative, or neutral sentiment. There are many potential applications of sentiment analysis:

* Customer Insights: Analyzing sentiment in customer feedback helps businesses understand customer satisfaction, preferences, and pain points. This information guides decision-making and improvements in products and services.

* Brand Reputation Management: Sentiment analysis allows organizations to monitor and manage their brand reputation. 

* Market Research: Sentiment analysis is valuable for market research, providing insights into consumer sentiment and emerging trends.

* Social Media Monitoring: Sentiment analysis helps businesses monitor sentiment on social media platforms, enabling real-time insights into public opinion, campaign effectiveness, and customer engagement.


For this project we will be analyzing comments from online cycling communities on reddit to determine the prevailing sentiment associated with each brand.

### Skills

- Python
- Logistic Regression
- Regularization, K Folds Cross-Validation
- Pandas, Sklearn, Statsmodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- ROC Curve, Classification Report,

# [Home Values vs Interest Rates](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/fred_project/fred_project.ipynb)

### **Project Overview**

The FRED API (Federal Reserve Economic Data API) provides access to a wide range of economic data from reliable sources such as government agencies and central banks. In this project we will use the FRED API to extract home sales and interest rate data. We will use python to process and combine the data in order to determine how rising interest rates have affected home prices in various geographic regions in the US. 

### Skills

- Python, Plotly, Numpy, Maptplotlib
- Pands, FRED API

# [Voter Turnout Model](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/voter_turnout_model)

### **Objective**

This purpose of this model is to assign a voting propensity score to each voter that corresponds to how likely they are to participate in a specific election. This solves two problems often faced by political campaigns. First, it provides an evidence-driven basis for building a "universe" of voters who will likely vote in an upcoming election. Secondly, the propensity score gives campaigns a basis on which they can segment and prioritize their outreach. For example, a campaign may choose to forego GOTV efforts on voters with propensity scores over 90%. That decision could free up resources which could be used to contact voters with lower propensity scores a second time, which will increase turnout. Propensity scores allow campaigns to easily plan their outreach according to their specific needs, and make it easy to modify those plans when the needs arises.

### **Project Features**

- Python
- Logistic Regression
- Regularization, K Folds Cross-Validation
- Pandas, Sklearn, Statemodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- ROC Curve, Classification Report,

# [Linear Regression from Scratch](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/linear_regression_from_scratch/%20linear_regression_scratch.ipynb)

### **Objective**

The purpose of this project is to gain a thorough understanding of linear regression by building a model from scratch. The most common way of recreating linear regression from scratch is to simply rewrite the formula in python, but I find that looking at the formula alone is not always enough to understand how it works. Instead, we will break the formula down into pieces that are easier to understand. We'll calculate one piece at a time, put the whole model together, and then check our work using seaborn and statsmodels.

### **Project Features**

- Python
- Pandas, Sklearn, Statemodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- Model construction, Correlation matrices, scatterplots

# [Predicting Diabetes with Logistic Regression Model](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/diabetes_logistic_regression)

### **Objective**

The purpose of this project is to build amodel that predicts whether a person will develop diabates based on health-related metrics.

### **Project Features**

- Python
- Pandas, Sklearn, Seaborn, Matplotlib, Jupyter Notebooks
- Logistic Regression, Correlation matrices, scatterplots

# [Movie Data Correlations](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/movie_data_correlation_testing)

### **Objective**

In this project we will examine IMDB data on thousands of movies to determine if any relationships exist between a movie's gross earnings and other attributes such as its budget, genre, rating etc.

### **Project Features**

- Python
- Pandas, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- Correlation matrices, scatterplots, heatmaps
- Linear regression

# [Image Classification Neural Network (Tensorflow)](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/image_classification_neural_network/image_classification_neural_network.ipynb)

### **Objective**

The objective of this project is to build, train, and test a neural network that can accurately classify the types of clothing appearing in images.

### **Project Features**
- Python
- Tensorflow, Keras, Numpy
- Neural Networks



Additional visualization projects can be found in my [Tableau portfolio.](https://public.tableau.com/app/profile/jon.biggerstaff)

# [Local Candidate Research Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/local_candidate_dashboard)

### **Objective**

Media and news outlets often neglect to cover state and local elections. As a result, most voters don’t know which candidates they are choosing between until they are completing their ballot. In this project we will design an interactive tool (in the form of a Tableau dashboard) that will allow voters in Colorado to quickly and easily find their state legislative districts, the candidates in those districts, and the relevant contact information. After election day, this dashboard can be easily modified to display the winning candidates. This will allow voters to easily see the legislators who represent them, allowing them to reach out to their local officials with questions or concerns.

### **Project Features**

- Python: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)


# [Political Committee Research Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/political_committee_research_dashboard)

### **Objective**

Every few years the US sets a new record for the most expensive election in our history. Billions of dollars flow into local, state, and national elections from countless different political organizations. Who are these organizations? Where does their money come from? What do they hope to accomplish? In this project we will build a dashboard that empowers Colorado voters with the answers to all of these questions, and  more.


### **Project Features**

- Python: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)

# [Spotify Data Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/spotify_dashboard)

### **Objective**

This is  a simple dashboard designed to visualize 10 years of music streaming history on Spotify. It features the TabCSS Tableau extension, which allows users to create styled backgrounds for dashboard objects and containers (rounded corners, color gradients etc). It uses Bootstrap CSS, Tailwind CSS color, and additional extended classes. Data cleaning was done with python.


### **Project Features**

- Python: (for data cleaning)
- Tableau (for data visualization and interactivity)
