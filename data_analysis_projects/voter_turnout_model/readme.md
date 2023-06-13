# Voter Turnout Model

### **Project Overview**

This purpose of this model is to assign a voting propensity score to each voter that corresponds to how likely they are to participate in a specific election. This solves two problems often faced by political campaigns. First, it provides an evidence-driven basis for building a "universe" of voters who will likely vote in an upcoming election. Secondly, the propensity score gives campaigns a basis on which they can segment and prioritize their outreach. For example, a campaign may choose to forego GOTV efforts on voters with propensity scores over 90%. That decision could free up resources which could be used to contact voters with lower propensity scores a second time, which will increase turnout. Propensity scores allow campaigns to easily plan their outreach according to their specific needs, and make it easy to modify those plans when the needs arises.

### Skills

- Python
- Logistic Regression
- Regularization, K Folds Cross-Validation
- Pandas, Sklearn, Statsmodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- ROC Curve, Classification Report,


### Method

The most important question I had to answer when building this model was whether or not it was possible to predict the turnout of a future election using only data from previous elections. After testing a few different methods, I found the best results using a similar election from the recent past as my dependent variable. I then evaluated the model's performance by comparing it to real-world election turnout data. That meant building the model around the 2019 municipal election, and evaluating performance based on turnout data from the 2023 election.

After cleaning and preprocessing the data and one-hot encoding the categorical variables , I was able to identify which independent variables to keep in the model by examining their respective coefficients using traditional (non machine learning) logistic regression. I then used sk-learn to test multiple classification models before settling on logistic regression. I used the GridSearchCV function to find the best hyperparameters for the model. Using sk-learn's classification report, I was able to tune the model to score around 89% consistently. 

However, as I mentioned in the first paragraph, the purpose of this model wasn't to use 2019 data to predict which people voted in 2019, it was to predict which voters will participate in the 2023 election. The only way to truly test performance of the model was to compare the model scores to the future turnout results in 2023.  To do that, I waited until the 2023 election data was available and then use a merge to combine the new turnout data with each voter's propensity score. I was then wrote a simple function to calculate my own real-world classification performance metrics.

For this use case, precision is what was most important. The model ended up scoring around 80%, though true usefulness of the model is more complex than simple classification metrics can measure. This model was used by a campaign to win a very competitive election during which we were able to use the scores to segment and prioritize various aspects of political outreach.
