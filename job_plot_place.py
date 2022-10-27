# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 13:06:22 2022

@author: user
"""
# import numpy as np
import pandas as pd
# from job_data_transform import job
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'mingliu'
job = pd.read_excel('104data0712Trans930.xlsx')
# 查看有哪些地區
city = job["jobCounty"].unique().tolist()
print(city)
# 取工作分配地區
city = ['桃園市', '台中市', '台北市', '新北市', '高雄市', '嘉義縣', '台南市', '新竹縣', '新竹市', '屏東縣', '彰化縣', '澎湖縣', '苗栗縣', '宜蘭縣', '嘉義市', '花蓮縣', '雲林縣']
citycount = []    

for i in range(len(city)):
    df1 = job[job['jobLoc'].str.contains(city[i])]
    citycount.append(len(df1))
    
ser = pd.Series(citycount,index = city)
print(ser)
plt.axis('off')
ser.plot(kind='pie',title = "工作地點分布",figsize=(6,6))
plt.show()


# 地區薪水平均值
salarylist = []
for i in range(len(city)):
    df1 = job[(job['jobLoc'].str.contains(city[i])) & (job['jobSal'])]
    indexlist = df1.index  #取得資料索引
    total = 0  #薪資總額
    for j in range(len(df1)):
        salary = df1['jobSal'][indexlist[j]]
        total += salary
    salarycity = int(total/len(df1))  #平均薪資
    salarylist.append(salarycity)



ser = pd.Series(salarylist, index=city)  #串列轉Series
print(ser)
plt.ylabel('單位：元')
ser.plot(kind='bar', title='各地區職缺平均薪資', figsize=(5, 5))  #繪製長條圖
plt.show()





# 地區薪水平均值

# salarylist = []
# for i in range(len(city)):
#     df1 = job[(job['jobLoc'].str.contains(city[i])) & (job['jobSal'].str.contains('月薪'))]
#     indexlist = df1.index  #取得資料索引
#     total = 0  #薪資總額
#     for j in range(len(df1)):
#         salarytem = df1['jobSal'][indexlist[j]].replace(',', '')  #以資料索引取得資料
#         salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
#         if len(salanum) == 1:  #若是1個數值即為薪資
#             salary = int(salanum[0])
#         else:  #若是2個數值則取平均數
#             salary = (int(salanum[0])+int(salanum[1]))/2
#         total += salary
#     salarycity = int(total/len(df1))  #平均薪資
#     salarylist.append(salarycity)

# ser = pd.Series(salarylist, index=city)  #串列轉Series
# print(ser)
# plt.ylabel('單位：元')
# ser.plot(kind='bar', title='六都電腦職缺薪資', figsize=(5, 5))  #繪製長條圖
# plt.show()