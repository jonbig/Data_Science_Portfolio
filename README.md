# Data Science Portfolio 


This repository is a portfolio of data science projects I’ve completed. Many of the projects are designed to solve real-world problems I’ve encountered in my political/advocacy career, other projects were completed for educational purposes. Python based projects are typically presented in Jupyter Notebooks, with the exception of ad hoc programs such as web scrapers built to gather data for specific projects. SQL projects will contain a read me markdown file that will walk through the project step by step. Each step will contain links to relevent SQL files. Data visualization projects will contain links to Tableau public where you can view and interact with the visualizations and dashboards.

All projects will follow a similar work flow:

1. **Ask** questions and define the problem.
2. **Prepare** data by collecting and storing the information.
3. **Process** data by cleaning and checking the information.
4. **Analyze** data to find patterns, relationships, and trends.
5. **Share** data with your audience.
6. **Act** on the data and use the analysis results.

Below you will find links to all projects each with a brief project summary. Thanks for visiting my portfolio!

_Note: Several of the Data Visualization Projects below are components of a larger political data project I named [Dark Money Spotlight](https://public.tableau.com/app/profile/jon.biggerstaff/viz/ColoradoPoliticalSpendingTracker2/DistrictDash). This project was designed to allow Colorado voters to easily evaluate the candidates and committees making political expenditures in their local districts. Thousands of Colorado voters used the Dark Money Spotlight website to research political candidates in advance of the 2022 midterm elections. The website has since been taken down, but you can still [access the political spending tracker here.](https://public.tableau.com/app/profile/jon.biggerstaff/viz/ColoradoPoliticalSpendingTracker2/DistrictDash) Please note the dashboards are not optimized for mobile._


# Data Analysis & Machine Learning

### [Voter Turnout Model](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/voter_turnout_model/final_2019_denver_model.ipynb)

### **Objective**

This purpose of this model is to assign a voting propensity score to each voter that corresponds to how likely they are to participate in a specific election. This solves two problems often faced by political campaigns. First, it provides an evidence-driven basis for building a "universe" of voters who will likely vote in an upcoming election. Secondly, the propensity score gives campaigns a basis on which they can segment and prioritize their outreach. For example, a campaign may choose to forego GOTV efforts on voters with propensity scores over 90%. That decision could free up resources which could be used to contact voters with lower propensity scores a second time, which will increase turnout. Propensity scores allow campaigns to easily plan their outreach according to their specific needs, and make it easy to modify those plans when the needs arises.

### **Project Features**

- Python
- Logistic Regression
- Regularization, K Folds Cross-Validation
- Pandas, Sklearn, Statemodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- ROC Curve, Classification Report,

### [Linear Regression from Scratch](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/linear_regression_from_scratch/%20linear_regression_scratch.ipynb)

### **Objective**

The purpose of this project is to gain a thorough understanding of linear regression by building a model from scratch. The most common way of recreating linear regression from scratch is to simply rewrite the formula in python, but I find that looking at the formula alone is not always enough to understand how it works. Instead, we will break the formula down into pieces that are easier to understand. We'll calculate one piece at a time, put the whole model together, and then check our work using seaborn and statsmodels.

### **Project Features**

- Python
- Pandas, Sklearn, Statemodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- Model construction, Correlation matrices, scatterplots

### [Predicting Diabetes with Logistic Regression Model](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/diabetes_logistic_regression)

### **Objective**

The purpose of this project is to build amodel that predicts whether a person will develop diabates based on health-related metrics.

### **Project Features**

- Python
- Pandas, Sklearn, Seaborn, Matplotlib, Jupyter Notebooks
- Logistic Regression, Correlation matrices, scatterplots

### [Movie Data Correlations](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_analysis_projects/movie_data_correlation_testing)

### **Objective**

In this project we will examine IMDB data on thousands of movies to determine if any relationships exist between a movie's gross earnings and other attributes such as its budget, genre, rating etc.

### **Project Features**

- Python
- Pandas, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- Correlation matrices, scatterplots, heatmaps
- Linear regression

### [Image Classification Neural Network (Tensorflow)](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/image_classification_neural_network/image_classification_neural_network.ipynb)

### **Objective**

The objective of this project is to build, train, and test a neural network that can accurately classify the types of clothing appearing in images.

### **Project Features**
- Python
- Tensorflow, Keras, Numpy
- Neural Networks

# Data Visualization

Additional visualization projects can be found in my [Tableau portfolio.](https://public.tableau.com/app/profile/jon.biggerstaff)

### [Local Candidate Research Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/local_candidate_dashboard)

### **Objective**

Media and news outlets often neglect to cover state and local elections. As a result, most voters don’t know which candidates they are choosing between until they are completing their ballot. In this project we will design an interactive tool (in the form of a Tableau dashboard) that will allow voters in Colorado to quickly and easily find their state legislative districts, the candidates in those districts, and the relevant contact information. After election day, this dashboard can be easily modified to display the winning candidates. This will allow voters to easily see the legislators who represent them, allowing them to reach out to their local officials with questions or concerns.

### **Project Features**

- Python: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)


### [Political Committee Research Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/political_committee_research_dashboard)

### **Objective**

Every few years the US sets a new record for the most expensive election in our history. Billions of dollars flow into local, state, and national elections from countless different political organizations. Who are these organizations? Where does their money come from? What do they hope to accomplish? In this project we will build a dashboard that empowers Colorado voters with the answers to all of these questions, and  more.


### **Project Features**

- Python: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)

### [Spotify Data Dashboard](https://github.com/jonbig/Data_Science_Portfolio/tree/main/data_visualization_projects/spotify_dashboard)

### **Objective**

This is  a simple dashboard designed to visualize 10 years of music streaming history on Spotify. It features the TabCSS Tableau extension, which allows users to create styled backgrounds for dashboard objects and containers (rounded corners, color gradients etc). It uses Bootstrap CSS, Tailwind CSS color, and additional extended classes. Data cleaning was done with python.


### **Project Features**

- Python: (for data cleaning)
- Tableau (for data visualization and interactivity)
