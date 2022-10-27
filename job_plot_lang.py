# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:36:57 2022

@author: user
"""

import pandas as pd  # 呼叫pandas程式套件
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'mingliu'
# 匯入資料
job = pd.read_excel('104data0712Trans930.xlsx')

# 資料整理和處理
job.drop_duplicates(subset='jobName',inplace=True)
job.dropna(axis=0,inplace=True)

# 各程式語言薪水平均值
lang = ['Java', 'Python', 'C#','PHP','JavaScript']

salarylist = []
for i in range(len(lang)):
    df1 = job[(job['jobKeyword'].str.contains(lang[i])) & (job['jobSal'])]
    indexlist = df1.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df1)):
        salary = df1['jobSal'][indexlist[j]]
        total += salary
    salarycity = int(total/len(df1))  #平均薪資
    salarylist.append(salarycity)


ser = pd.Series(salarylist, index=lang)  #串列轉Series
print(ser)
plt.ylabel('單位：元')
ser.plot(kind='bar', title='各程式語言平均職缺薪資', figsize=(5, 5))  #繪製長條圖
plt.show()



# 各程式語言盒鬚圖
# sns 畫法
import seaborn as sns
langcount = []  
job.drop(job[job["jobSal"] > 150000].index,inplace=True) 

sns.set(style="whitegrid")
ax = sns.boxplot(x = "jobKeyword", y = "jobSal", width=0.2, data = job, palette = "Set3")

java = job[job['jobKeyword']=='Java']
# print(java)
j = java['jobSal']
# java = pd.Series(j)
# print(java)
print("Java 下四分位數 Q1 = ",j.quantile(0.25))
print("Java 中位數 Q2 = ",j.quantile(0.5))
print("Java 上四分位數 Q3 = ",j.quantile(0.75))
# 第25至第75個百分點，有50%的數據在IQR之間
print("Java 四分位間距 IQR = ",j.quantile(0.75)-j.quantile(0.25))
# 最小值區間（maximum）：Q1 - 1.5 * IQR
# 最大值區間（maximum）：Q3 + 1.5 * IQR

print()
python = job[job['jobKeyword']=='Python']
p = python['jobSal']
print("Python 下四分位數 Q1 = ",p.quantile(0.25))
print("Python 中位數 Q2 = ",p.quantile(0.5))
print("Python 上四分位數 Q3 = ",p.quantile(0.75))
print("Python 四分位間距 IQR = ",p.quantile(0.75)-p.quantile(0.25))
print()
php = job[job['jobKeyword']=='PHP']

p = php['jobSal']
print("PHP 下四分位數 Q1 = ",p.quantile(0.25))
print("PHP 中位數 Q2 = ",p.quantile(0.5))
print("PHP 上四分位數 Q3 = ",p.quantile(0.75))
print("PHP 四分位間距 IQR = ",p.quantile(0.75)-p.quantile(0.25))

print()
c = job[job['jobKeyword']=='C#']
p = c['jobSal']
print("C# 下四分位數 Q1 = ",p.quantile(0.25))
print("C# 中位數 Q2 = ",p.quantile(0.5))
print("C# 上四分位數 Q3 = ",p.quantile(0.75))
print("C# 四分位間距 IQR = ",p.quantile(0.75)-p.quantile(0.25))

print()
c = job[job['jobKeyword']=='JavaScript']
p = c['jobSal']
print("JavaScript 下四分位數 Q1 = ",p.quantile(0.25))
print("JavaScript 中位數 Q2 = ",p.quantile(0.5))
print("JavaScript 上四分位數 Q3 = ",p.quantile(0.75))
print("JavaScript 四分位間距 IQR = ",p.quantile(0.75)-p.quantile(0.25))


# matplot 畫法
# job.drop(job[job["jobSal"] > 150000].index,inplace=True) 



# plt.boxplot([job[job['jobKeyword']=='Java'].jobSal, 
#              job[job['jobKeyword']=='Python'].jobSal, 
#              job[job['jobKeyword']=='C#'].jobSal, 
#              job[job['jobKeyword']=='PHP'].jobSal, 
#              job[job['jobKeyword']=='JavaScript'].jobSal], 
#             labels = ['Java', 'Python', 'C#','PHP','JavaScript'])

# plt.ylabel('jobSal')
# plt.show()