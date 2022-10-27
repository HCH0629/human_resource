# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:52:05 2022

@author: user
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import mean_absolute_error
from sklearn import metrics

plt.rcParams['font.sans-serif'] = 'mingliu'

job = pd.read_excel('104data0712Trans930.xlsx')

job.drop_duplicates(subset='jobName',inplace=True)
job.dropna(axis=0,inplace=True)
job.drop(job[job["jobSal"] > 150000].index,inplace=True) 
job.drop(job[job["jobSal"] < 38000].index,inplace=True) 

job_corr = job.corr()

X = job[['jobExp',
         "LangTrans",
         "CountyTrans"]]

y = job['jobSal']
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=19)

std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)

std_y = StandardScaler()
y_train = std_y.fit_transform(y_train.values.reshape(-1, 1))
y_test = std_y.transform(y_test.values.reshape(-1, 1))

lr = LinearRegression()
lr.fit(x_train, y_train)
print('權重值：{}'.format(lr.coef_)) 
print('偏置值：{}\n'.format(lr.intercept_))
y_predict = std_y.inverse_transform(lr.predict(x_test))
y_real = std_y.inverse_transform(y_test)

for i in range(10):
    print('預測值{}：{}，真實值：{}'.format(i+1, y_predict[i], y_real[i]))

merror = metrics.mean_squared_error(y_real, y_predict)
print('MSE 平均方差：{}'.format(merror))

merror = metrics.mean_squared_error(y_real, y_predict)
print('RMSE 均方根誤差：{}'.format(np.sqrt(merror)))

# MAE:
# 範圍[0,+∞)，當預測值與真實值完全吻合時等於0，即完美模型；誤差越大，該值越大。
merror = metrics.mean_absolute_error(y_real, y_predict)
print('MAE 平均絕對誤差：{}'.format(merror))


# MAPE:
# 範圍[0,+∞)，MAPE 爲0%表示完美模型，MAPE 大於 100 %則表示劣質模型。MAPE 的值越小，說明預測模型擁有更好的精確度.
def mape(y_true, y_pred):
    return np.mean(np.abs((y_pred - y_true) / y_true)) * 100

print('MAPE 平均百分比誤差：',mape(y_real, y_predict))

# SMAPE
def smape(y_true, y_pred):
    return 2.0 * np.mean(np.abs(y_pred - y_true) / (np.abs(y_pred) + np.abs(y_true))) * 100

print('smape score: ',smape(y_real, y_predict)) 

from sklearn.metrics import r2_score
print('R2 score: ',r2_score(y_real,y_predict))
print('R2 score: ', lr.score(x_train, y_train))

#  ==================================================================================

# lr = LinearRegression()
# lr.fit(x_train, y_train)
# y_predict = lr.predict(x_test)
# print('權重值：{}'.format(lr.coef_)) 
# print('偏置值：{}\n'.format(lr.intercept_))
# # for i in range(1):
# #     print('預測值{}：{}，真實值：{}'.format(i+1, y_predict[i], y_test[i]))
# # 查看其預測分數
# print('R2 score: ', lr.score(x_train, y_train))
# mse = metrics.mean_squared_error(y_test, y_predict)
# print('MSE score: ', mse)
