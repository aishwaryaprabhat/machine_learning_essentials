# Time Series Analysis and Forecasting

## Overview

### What is a time series?
A time series is a set of observations taken at specified times usually at equal intervals. It is used to predict the future values based on the previous observed values.


### What are some applications on time series forecasting?
- Business forecasting
- Understanding past behaviour
- Future planning
- Evaluate current accomplishment

### What are the characteristics of time series?

#### 1. Trend
Trend is a general movement of values in upward or downward direction over a long period of time. For example: during summers, the daily temperatures generally have an upward trend in the first few months and then a downward trend as autumn approaches. 

#### 2. Seasonality
Upward or downward swings that is a repeating pattern during a fixed period of time. For example: ice cream sales always cyclically go up during summer and down during winter.

#### 3. Irregularity/Noise
Erratic unsystematic changes in values. 

#### 4. Cyclic
Repeating up and down movement but unlike seasonality, these changes are not constrained by regularity of time period. They might reoccur in a year or two years or more or less. Eg: business cycles.

### When not to use time series analysis and forecasting?
- Values are constant
- Values are in the form of a neat functions 


## Stationarity

### What is stationarity?

Stationarity refers to the characteristic of a time series such that if a time series has a particular behaviour over time, there is a very high probability that it will follow the same in the future. It has a few 'rules':
1. Constant mean
2. Constant Variance
3. Autocovariance that does not depend on time 


### How do we test for stationarity?

1. Rolling statistics: plot the moving average or moving varianve and see if it varies with time. More of a visual technique
2. ADF (Agumented Dickey-Fuller) Test: Null hypothesis is that the TS is non-stationary. The test computes a test statistic, if the test statistic is less than the critical value the null hypothesis is rejected

## ARIMA Model

- AR: Auto Regressive model
	- Computes the correlation between value at t and t-1, t-2 etc.
	- p: refers to auteregressive lags

- MA: Moving average model
	- Average forecast of the noise
	- q: moving average

- I: Integration, binds the AR and MA
	- To enforce stationarity
	- d: order of integration 