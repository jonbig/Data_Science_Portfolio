Brand Reputation Management: Sentiment analysis allows organizations to monitor and manage their brand reputation. 

Market Research: Sentiment analysis is valuable for market research, providing insights into consumer sentiment and emerging trends.

Social Media Monitoring: Sentiment analysis helps businesses monitor sentiment on social media platforms, enabling real-time insights into public opinion, campaign effectiveness, and customer engagement.


For this project we will be analyzing comments from online cycling communities on reddit to determine the prevailing sentiment associated with each brand.

### Skills

- Python
- Logistic Regression
- Regularization, K Folds Cross-Validation
- Pandas, Sklearn, Statsmodels, Seaborn, Numpy, Matplotlib, Jupyter Notebooks
- ROC Curve, Classification Report,


### Method

The first step is to gather text data from the r/cycling and r/bicyling subreddits using the Python Reddit API Wrapper, or PRAW. Reddit allows me to pull data from 1,000 submissions for each subreddit, for a total of 2,000 of the most popular submission in reach subreddit. I was then able to extract all of the comments associated with each submission, for a total of around 270,000 comments. The next step was to extract every comment that mentions a cycling brand, and then build a dataframe with those comments paired with the cycling brand(s) they mentioned. After cleaning and preprocessing the data, it was time to determine the sentiment for each comment. 

The RoBERTa model, short for "Robustly Optimized BERT Approach," is a transformer-based neural network model for natural language processing. The RoBERTa model is pre-trained on a large corpus of unlabeled text, where it learns to understand the patterns and semantics of language. After running each comment through the RoBERTa model, I am given a positive sentiment score, negative sentiment score, and a neutral sentiment score.

To determine the sentiment for each cycling brand, I averaged the positive and negative sentiment scores for each brand's associated comments and graphed the results.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/cycling_brand_sentiment/cycling_brands_chart.PNG)
