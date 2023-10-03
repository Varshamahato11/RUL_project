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

### Assumptions

❏ Every engine is assumed to be at the 100% health initially.

❏ Engine health degrades with time.

❏ At cycles = 0, engine health = 1

❏ When RUL becomes zero in training set, i.e. engine completes all the cycles, engine health is assumed to be zero.

❏ To identify the features, which have a major impact on the engine’s health, we preprocess the data and compare slopes of all the graphs. (These features are assumed to exhibit change in data as time (or cycles) increases).

### RESULTS

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/44da983e-c1ac-4547-b011-7b4be0aa1e83)

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/a091d514-e864-4ce1-9e19-044f70f443d7)


![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/14cc7bce-5ccf-4f83-b94b-2650bbc76bb0)

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/f083c2ee-fa5f-4ff2-955c-7c4f730a8a75)


![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/53b43016-0eec-4976-b2c0-39ca854c3909)

![image](https://github.com/Varshamahato11/RUL_project/assets/90463649/73329aa8-e445-4c00-8ddb-495909428974)


### INSTALLATION STEPS:

```
  conda create -p venv python==3.9 -y
```

```
  conda activate venv/
```

```
  pip install -r requirements.txt
```

### Deployment

```
  python application.py
```




