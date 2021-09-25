import numpy as np # linear algebra
import pandas as pd # data processing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from pandas import DataFrame,Series
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split,cross_val_score, cross_val_predict
import missingno as msno # plotting missing data
import seaborn as sns # plotting library
from sklearn import svm

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

dataset = pd.read_csv("/home/ec2-user/environment/code/week11_ml/cars.csv")
dataset.describe()

# Finding all the columns with NULL values
dataset.replace([np.inf, -np.inf], np.nan, inplace=True)
dataset.isna().sum()
# Drop the rows with missing values
dataset = dataset.dropna(how='any',axis=0)

dataset = dataset.reset_index()

fig = sns.pairplot(dataset[['age', 'miles', 'debt', 'income', 'sales']], diag_kind="kde")

# fig = sns_plot.get_figure()
fig.savefig("models_visualize2.png")


train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)


# Calculating basic statistics with the train data
train_stats = train_dataset.describe()
train_stats.pop("sales") # excluding the dependent variable
train_stats = train_stats.transpose()
train_stats


# Creating the normalizing function with mean and standard deviation
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']
  
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


train_labels = train_dataset.pop("sales") # using .pop function to store only the dependent variable
test_labels = test_dataset.pop("sales")
x_train=normed_train_data
x_test=normed_test_data
y_train=train_labels
y_test=test_labels


# lin_reg = LinearRegression()
# lin_reg.fit(x_train,y_train)
# #Prediction using test set 
# y_pred = lin_reg.predict(x_test)
# mae=metrics.mean_absolute_error(y_test, y_pred)
# mse=metrics.mean_squared_error(y_test, y_pred)
# # Printing the metrics
# print('R2 square:',metrics.r2_score(y_test, y_pred))
# print('MAE: ', mae)
# print('MSE: ', mse)


dt_regressor = DecisionTreeRegressor(random_state = 0)
dt_regressor.fit(x_train,y_train)
#Predicting using test set 
y_pred = dt_regressor.predict(x_test)
mae=metrics.mean_absolute_error(y_test, y_pred)
mse=metrics.mean_squared_error(y_test, y_pred)
# Printing the metrics
print('Suppport Vector Regression Accuracy: ', dt_regressor.score(x_test,y_test))
print('R2 square:',metrics.r2_score(y_test, y_pred))
print('MAE: ', mae)
print('MSE: ', mse)


