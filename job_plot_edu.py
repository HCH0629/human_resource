# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:50:11 2022

@author: user
"""

# import numpy as np
import pandas as pd
# from job_data_transform import job
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'mingliu'
job = pd.read_excel('104data0712Trans930.xlsx')
# 查看有哪些地區
edu = job["jobEdu"].unique().tolist()
print(edu)
# 取工作分配地區
edu = ['碩士', '高中', '大學']


# 學歷薪水平均值
salarylist = []
for i in range(len(edu)):
    df1 = job[(job['jobEdu'].str.contains(edu[i])) & (job['jobSal'])]
    indexlist = df1.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df1)):
        salary = df1['jobSal'][indexlist[j]]
        total += salary
    salarycity = int(total/len(df1))  #平均薪資
    salarylist.append(salarycity)



ser = pd.Series(salarylist, index=edu)  #串列轉Series
print(ser)
plt.ylabel('單位：元')
ser.plot(kind='bar', title='學歷的平均薪資', figsize=(5, 5))  #繪製長條圖
plt.show()