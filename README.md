# Los Angeles Crime Forecasting

**Authors**: [David Bruce](mailto:david.bruce14@gmail.com), [Sidney Kung](mailto:sidneyjkung@gmail.com), [Lhamu Tsering](mailto:boutlhamu@gmail.com)

![img](./visualizations/los-angeles-us-banner-dp-min.png)

## Overview
This summer (2020) saw a historic rise of demonstrations across the United States calling to 'Defund the Police.' Los Angeles Mayor, Eric Garcetti, reversed the trend of increasing police spending for the first time in years by reducing the Los Angeles Police Department (LAPD) budget by $150 million ([NY Times](https://www.nytimes.com/interactive/2020/06/12/upshot/cities-grew-safer-police-budgets-kept-growing.html)). Using the most recent data on crime made available by the City of Los Angeles ([data.lacity.org](https://data.lacity.org/Public-Safety/Crime-Data-from-2010-to-2019/63jg-8b9z)) from January 2010 - June 2019, we used univariate time series modeling to forecast reported crime in Los Angeles to determine recent crime trends in LA. Working with AR, MA, ARMA, and SARIMA models we determined the best fit with the lowest AIC score. Then evaluated our best model, a SARIMA model, using RMSE and AIC. The final model had an RMSE of 24.66. 

## Business Problem

Los Angeles has the third largest police department in the country, with jurisdiction over almost 4 million people. The [People’s Budget LA](https://peoplesbudgetla.com/) and other community movements have worked to push local government to search for alternative social service solutions to public safety. We set out to justify this divestment with time series predicting and forecasting. Through additional analysis of the data we identify which areas and populations in LA have been hit the hardest by crime in the last 9 years, so that budget resources can be reallocated to social services in those high-impact communities.

## Data & Methods

![img](./visualizations/Monthly%20Crime%20Trend%20lineplot%20and%20dotplot.png)

This dataset is the [LA Crime & Arrest Data](https://www.kaggle.com/cityofLA/los-angeles-crime-arrest-data) from Kaggle. It reflects incidents of crime in Los Angeles dating from 2010 to mid-2019. The data is transcribed from original crime reports that may contain inaccuracies.

This was a univariate time series problem, predicting the monthly average crime count for each year. Time series model iterations included AR, ARMA and SARIMA algorithms. We compared the models against each other using the AIC score, and evaluated the final model with RMSE. The RMSE simply measures how accurate predictions are.  We predicted data through 2019, because short-term predictions can aid immediate decisions for the business context.

## Business Questions
**1. How much has crime fluctuated in the last 8 years?**

![img](./visualizations/LA_Volume_of_Crime_Trend_boxplot.png)

The average monthly crime in the period between 2010 and 2018 ranges between 530 crimes per month to 630 crimes per months. We can also see that 2017 saw the highest average number of crimes reported, while 2013 saw the lowest average number of crimes reported in LA.


**2. What areas in LA have the highest crime rate?**

![img](./visualizations/LA_crime_map.png)

The top 5 areas where most of the crimes in LA have occured among the 21 geographic areas is 77th Street, Southwest, North Hollywood, Pacific, and Southeast.


**3. What are the top 3 vulnerable demographics in LA?**

![img](./visualizations/Distribution_of_victims_by_descent_and_area_name.png)

For all the crimes reported between 2010 and June of 2019, at 34%, victims of Latinx descent account for the highest number of victims of crimes in that period. White victims account for 24% and Black victims account for 16% of all crime victims in that period.

Looking at the top 3 vulnerable demographics in LA, Black and Latinx communities has most suffered in the highest crime occuring areas of 77th Street and Southeast. This could also be that there are lesser White people living in these two areas. White victims are highest in the North Hollywood, Pacific areas. Again, this could be because these areas have higher white population. Similarly, areas such as Mission, Newton, Rampart, Foothill and Hollenbeck have a higher number of Latinx victims than the other descents.

## Final Model Performance

To get to our final model, we first analysed the time series data for stationarity  as well as stationarity in the residuals of the time series. We also identified trend and seasonality in the data by performing a seasonal decomposition of the time series. On multiple iterations of differencing on the time series, we were not able to achieve stationarity. However, since the residuals were stationary we went further into the modeling process. Below is a table that shows you the main model iterations that were compared to identify the best final model.

To make predictions and forecast the time series data, we want a model that minimizes error. Therefore, to compare models for model selection we picked the AIC score and the RMSE score. The lower these measures the better the model.

![img](./visualizations/model_iterations.png)

Referring to the table above, we saw that there was a relatively small difference in the model RMSE of our previous best model ARMA-3,5 vs SARIMAX(0, 2, 2)x(2, 2, 2, 12). However, the AIC for the SARIMAX(0, 2, 2)x(2, 2, 2, 12) is significantly lower, indicating a better fit model. Therfore, our final best model is the SARIMAX(0, 2, 2)x(2, 2, 2, 12).

![img](./visualizations/final_model_forecasts.png)

Once the final model was predicted we ran a diagnostic to confirm that the residuals pass the assumptions of zero mean and weak correlation. The residuals from our best model passed the assumptions implying that the model uses all information in the data to make forecasts and that the forecasts are unbiased.

On plotting the forecast as shown in the image above, we find that as the number of forecast steps (here steps =24) are increased the forecasted values stray above and away from the observed values. The confidence interval (shaded area) for the forecasts also exponentially increase with additional number of steps.
## Recommendations
Our recommendations stem primarily from our explorative data analysis. The forecasts our model predicted predicts a slight decrease in crime for 2019.

1. Based on the limited forecasting power of our univariate model, we recommend compiling more historical data to build stronger predictive power

2. Funding formerly allocated to the LAPD should be redistributed to social service solutions to public safety problems in the highlighted areas (77th Street, Southwest, and North Hollywood).

3. Communities of color, namely Black and Latinx, makeup larger portions of the victims in these high-crime areas and should receive small business loans and other community-based incentives to help revitalize these areas.

## Next Steps
- With more time we would acquire more historical data to help make stronger predictions and forecasts further into the future. 
- The addition of exogenous variables from census data would also add some complexity to our univariate model that could help us to diagnose underlying issues with crime more directly. 
- Using a SARIMAX model or experimenting with Facebook Prophet would be of interest, and using incoming data to evaluate our model's forecasting performance.


## Repository Contents
- `EDA`: Folder contains exploratory data analysis notebooks
- `data`: Folder contains data used in notebooks, mostly hidden in .gitignore due to file sizes
- `modeling`: Folder contains different stages of modeling
- `src`: Folder contains .py file
- `visualizations`: Folder contains graphs from EDA & modeling process
- `.gitignore`: Contains hidden files including the original dataset
- `data_cleaning.ipynb`: Notebook used to clean `crime-data-from-2010-to-present.csv`
- `data_loading.ipynb`: Notebook used to load in Kaggle data
- `final_notebook.ipynb`: Final notebook with EDA analysis and modeling process
