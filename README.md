# Remaining Useful Life (RUL) Prediction for Turbofan Engines

### Objective
The objective of this project is to develop a machine learning model to predict the remaining useful life of aircraft turbofan engines. The Remaining Useful Life (RUL) is the amount of cycles an engine has left before it needs maintenance.

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/047a8bbd-ad1a-40b4-b17d-b72c80f0161c)

### Project Description
In industry, prognostics and health management are key topics for anticipating asset state and avoiding downtime and breakdowns. Run-to-Failure simulation data from turbofan jet engines is included.
The C-MAPSS software was used to simulate engine degradation. Four separate sets of operational conditions and fault modes were simulated in four different ways. To characterize fault progression, record numerous sensor channels. The Prognostics CoE at NASA Ames provided the data set.

Abstract

❏ NASA released dataset of 218 turbofan engines in 2008. The data was recorded until the point of breakdown.

❏ In this project, we would try to understand the data-set, and predict Remaining Useful Life (RUL) of engines from testing data.

❏ We would try to deploy several machine learning models on this data-set, and discuss their performance. And finally, we would try to solve this problem using a mix-match of various algorithms to the best of our knowledge

### About Data

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/875d57e6-3dc2-4bf8-b744-19034691cc18)

❏ Training data was a matrix of 45918 X 26

❏ It consisted of data form 218 engines, until breakdown.

❏ Training data had following features:

❏ Unit number of engine

❏ nth cycle in operation

❏ 3 operational settings

❏ 21 sensor’s readings

❏ Each unit number was associated with a specific engine
