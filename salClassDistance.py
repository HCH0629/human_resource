# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:17:43 2022

@author: user
"""

import pandas as pd
## 導入Python的數據處理套件
# import numpy as np
# import pandas as pd
## 導入視覺化套件
import matplotlib.pyplot as plt
from sklearn import metrics
## 導入Sklearn中的線性模組
# from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
## 將數據集分成訓練集與測試集的套件
from sklearn.model_selection import train_test_split
import seaborn as sns

job = pd.read_excel('104data0712Trans951.xlsx')

# ============================================================================

# 將薪水轉換為級距
sal_df = job[['jobSal']] 
for j in range(len(sal_df)):
    pay = sal_df.at[j,'jobSal']
    if  20000 <= pay < 30000:
        sal_df.at[j,'jobSal'] = 0
    elif 30000 <= pay < 40000:
        sal_df.at[j,'jobSal'] = 1
    elif 40000 <= pay < 50000:
        sal_df.at[j,'jobSal'] = 2
    elif 50000 <= pay < 60000:
        sal_df.at[j,'jobSal'] = 3
    elif 60000 <= pay < 70000:
        sal_df.at[j,'jobSal'] = 4
    elif 70000 <= pay < 80000:
        sal_df.at[j,'jobSal'] = 5
    elif 80000 <= pay < 90000:
        sal_df.at[j,'jobSal'] = 6
    else:
        sal_df.at[j,'jobSal'] = 7

job['classDistance'] = sal_df
job[['classDistance']] = job[['classDistance']].astype(float)
# 更改欄位的順序
columns_name = job.columns.tolist()
columns_name.insert(columns_name.index('jobSal')+1, 
                    columns_name.pop(columns_name.index('classDistance')))
job = job[columns_name]

job.drop_duplicates(subset='jobName',inplace=True)
job.dropna(axis=0,inplace=True)

job_corr = job.corr()

## 定義自變量與應變量
X = job[['jobExp',
         "LangTrans",
         "CountyTrans",
         "classDistance"]]

y = job['classDistance']


# 繪製特徵與標籤組合的散點視覺化
sns.pairplot(data=X ,diag_kind='hist', hue= 'classDistance')
plt.show()



# 選取其前三個特徵繪製三維散點圖
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

class0 = X[X['classDistance']==0].values
class1 = X[X['classDistance']==1].values
class2 = X[X['classDistance']==2].values
class3 = X[X['classDistance']==3].values
class4 = X[X['classDistance']==4].values
class5 = X[X['classDistance']==5].values
class6 = X[X['classDistance']==6].values
class7 = X[X['classDistance']==7].values

# 'setosa'(0), 'versicolor'(1), 'virginica'(2)
ax.scatter(class0[:,0], class0[:,1], class0[:,2], label='class0')
ax.scatter(class1[:,0], class1[:,1], class1[:,2], label='class1')
ax.scatter(class2[:,0], class2[:,1], class2[:,2], label='class2')
ax.scatter(class3[:,0], class3[:,1], class3[:,2], label='class3')
ax.scatter(class4[:,0], class4[:,1], class4[:,2], label='class4')
ax.scatter(class5[:,0], class5[:,1], class5[:,2], label='class5')
ax.scatter(class6[:,0], class6[:,1], class6[:,2], label='class6')
ax.scatter(class7[:,0], class7[:,1], class7[:,2], label='class7')
plt.legend()

plt.show()


## 將數據集分成訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


## 建立邏輯迴歸模型
model = LogisticRegression(random_state=0, solver='lbfgs')

## 擬和數據
model.fit(X_train, y_train)
print('the weight of Logistic Regression:',model.coef_)
print('the intercept(w0) of Logistic Regression:',model.intercept_)


train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

train_predict_proba = model.predict_proba(X_train)
test_predict_proba = model.predict_proba(X_test)

print('The test predict Probability of each class:\n',test_predict_proba)
## 其中第一列代表預測為0類的概率，第二列代表預測為1類的概率，第三列代表預測為2類的概率。

## 利用accuracy（準確度）【預測正確的樣本數目佔總預測樣本數目的比例】評估模型效果
print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_train,train_predict))
print('The accuracy of the Logistic Regression is:',metrics.accuracy_score(y_test,test_predict))

test_score = model.score(X_test, y_test) * 100
print("test_score",test_score)
## 檢視混淆矩陣
confusion_matrix_result = metrics.confusion_matrix(test_predict,y_test)
print('The confusion matrix result:\n',confusion_matrix_result)

# 利用熱力圖對於結果進行視覺化
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix_result, annot=True, cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.show()