# [Ozone Forecasting Model](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/voter_turnout_model/final_2019_denver_model.ipynb)

### **Project Overview**

At ground level, ozone is a pollutant and a component of smog. It forms through chemical reactions involving sunlight, nitrogen oxides (NOx), and volatile organic compounds (VOCs) emitted by various sources such as vehicles and industries. High levels of ground-level ozone can cause respiratory issues and worsen conditions like asthma and COPD. Monitoring ozone levels helps assess overall air pollution and the effectiveness of pollution control measures.

The goal of this project is to use time series data to build a model to forecast how much ozone will be present in the air of Los Angeles, CA. 

### Skills

- Python, Prophet, Sklearn
- Pandas, matplotlib, numpy, seaborn


### Method
The data I will be using for this project come from the EPA. It contains 10 years of hourly Ozone measurements in Los Angeles, CA. After cleaning the data and doing some exploratory analysis, I will use Meta's prophet model to predict future EPA measurements. I will build visualizations to test the model and then calculate the mean squared error and the mean absolute error to measure the model's performance.  At first glance we can already see a clear pattern in the data:

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/output.png)

Ozone formation is driven by sunlight. During the summer months, there is generally more intense and longer duration of sunlight, providing the necessary energy for chemical reactions that produce ozone. We can also see this pattern by looking at a box plot of the data.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/output2.png)

After training the model on 80% of the data, I will plot it's predictions in blue on top of the actual test measurements in read. This will give is a visual idea of how well the model is performing.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/output3.png)

The model appears to be capturing the majority of the ozone fluctuations while missing the measurements on the extremes, especially during the summer months. Let's zoom in to a week in February.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/output4.png)

While the model's performance in summer may be lacking,  we can see here that it does perform better during the winter. The first performance metric we will use is the mean squared error:

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/msd.PNG)

The square root of the MSE of the model is 0.013 ozone parts per million. Our data for 10 years ranges from 0. to 0.15 parts per million. Ozone concentrations above 0.07 are considered unhealthy. If our model predicted 0.04PPM we could expect the actual ozone level to be as high as 0.053 or as low as 0.027. A more intuitive way to evaluate the performance may be the mean absolute percent error:

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/mae.PNG)

The mean absolute percent error for this model is 0.0101%. The prophet model also allows me to zoom in on various compnents of the model's predictions:

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/ozone_prediction_model/output5.png)

While the model is predicting the overall trend to be flat, the shorter time frames tell a different story. The weekly chart indicates that ozone is higher on the weekends. This phenomenon is called the "Ozone Weekend Effect" and is caused by a reduction of diesel traffic on the roadways- which is very counterintuitive. The yearly and daily charts a little more predictable, showing higher ozone levels during the hottest parts of the year and the most active times of the day.


