# [Ozone Forecasting Model](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/voter_turnout_model/final_2019_denver_model.ipynb)

### **Project Overview**

At ground level, ozone is a pollutant and a component of smog. It forms through chemical reactions involving sunlight, nitrogen oxides (NOx), and volatile organic compounds (VOCs) emitted by various sources such as vehicles and industries. High levels of ground-level ozone can cause respiratory issues and worsen conditions like asthma and COPD. Monitoring ozone levels helps assess overall air pollution and the effectiveness of pollution control measures.

The goal of this project is to use time series data to build a model to forecast how much ozone will be present in the air of Los Angeles, CA. 

### Skills

- Python, Prophet, Sklearn
- Pandas, matplotlib, numpy, seaborn


### Method
The data I will be using for this project come from the EPA. It contains 10 years of hourly Ozone measurements in Los Angeles, CA. After cleaning the data and doing some exploratory analysis, I will use Meta's prophet model to predict future EPA measurements. I will build visualizations to test the model and then calculate the mean squared error and the mean absolute error to measure the model's performance. 
