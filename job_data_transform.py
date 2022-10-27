# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:39:44 2022

@author: user
"""

import pandas as pd
import re

job = pd.read_excel('104data0712.xlsx')


# =====================================================================================
# 將主要工具轉換為數字
tool_df = job[['jobName','jobKeyword','jobTool']]
for j in range(len(tool_df)):
    tool = tool_df.at[j,'jobKeyword']
    if tool.lower() in tool_df.at[j,'jobTool'].lower() :
        tool_df.at[j,'jobKeyword'] = tool
        
    elif tool.lower() in tool_df.at[j,'jobName'].lower():
        tool_df.at[j,'jobKeyword'] = tool
        
    else:
        tool_df.at[j,'jobKeyword'] = None


job['jobKeyword'] = tool_df[['jobKeyword']]
MainTool = job["jobKeyword"].unique().tolist()
job["KeywordTrans"] = job["jobKeyword"].apply(lambda x:MainTool.index(x))
# 更改欄位的順序
columns_name = job.columns.tolist() # 把df的欄位名稱，取出來放到一個list
columns_name.insert(columns_name.index('jobKeyword')+1, 
                    columns_name.pop(columns_name.index('KeywordTrans'))) # (第一個參數 insert 到想放入的地方, pop調原本的值)
job = job[columns_name] # 重新指定 指定好的順序
    
# =====================================================================================


# 將地區轉換為數字
place = job["jobCounty"].unique().tolist()
job["CountyTrans"] = job["jobCounty"].apply(lambda x:place.index(x))
# 更改欄位的順序
columns_name = job.columns.tolist()
columns_name.insert(columns_name.index('jobCounty')+1, 
                    columns_name.pop(columns_name.index('CountyTrans')))
job = job[columns_name]


# 不知道下面兩種方法，會不會構成線性回歸的影響
# 將教育程度轉換為數字，這邊隨意指定一個數字 比較無法感受到學士和碩士的大小差異
# num = job["jobEdu"].unique().tolist()
# job["jobEduTransform"] = job["jobEdu"].apply(lambda x:num.index(x))
        
edu_df = job[['jobEdu']]
for j in range(len(edu_df)):
    edu = edu_df.at[j,'jobEdu']
    if "博士" in edu:
        edu_df.at[j,'jobEdu'] = "博士"
    elif "碩士" in edu:
        edu_df.at[j,'jobEdu'] = "碩士"
    elif "大學" in edu :
        edu_df.at[j,'jobEdu'] = "大學"
    else:
        edu_df.at[j,'jobEdu'] = "高中"
job['jobEdu'] = edu_df

# 將教育程度轉換為數字
# 這邊是想要將碩士指定為2，學士指定為1 我認為他們是有大小的差異

num = {"博士":3, "碩士":2, "大學":1 ,"高中":0}
job["EduTrans"] = job["jobEdu"].map(num)
# 更改欄位的順序
columns_name = job.columns.tolist()
columns_name.insert(columns_name.index('jobEdu')+1, 
                    columns_name.pop(columns_name.index('EduTrans')))
job = job[columns_name]

#  ===========================================================================

# 將是否外派轉換為數字
trip_df = job[['jobBusinessTrip']]

for j in range(len(trip_df)):
    trip = trip_df.at[j,'jobBusinessTrip']
    trip = str(trip)
    if '無需出差外派' in trip:
        trip_df.at[j,'jobBusinessTrip'] = 0
    elif ('需出差' in trip) or ('需外派' in trip):
        trip_df.at[j,'jobBusinessTrip'] = 1
    else:
        trip_df.at[j,'jobBusinessTrip'] = 1
        
    
job['TripTrans'] = trip_df
job[['TripTrans']] = job[['TripTrans']].astype(float)
# 更改欄位的順序
columns_name = job.columns.tolist()
columns_name.insert(columns_name.index('jobBusinessTrip')+1, 
                    columns_name.pop(columns_name.index('TripTrans')))
job = job[columns_name]

#  ===========================================================================

# 將薪水轉換為數字
sal_df = job[['jobSal']] # job['jobSal'] 資料型態為Series 差別在有幾個中掛弧
for j in range(len(sal_df)):
    pay = sal_df.at[j,'jobSal']
    if '月薪' in pay:
        salarytem = sal_df.at[j,'jobSal'].replace(',', '')  #以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
        if len(salanum) == 1:  #若是1個數值即為薪資
            salary = int(salanum[0])
            sal_df.at[j,'jobSal'] = salary
        else:  #若是2個數值則取平均數
            salary = (int(salanum[0])+int(salanum[1]))/2
            sal_df.at[j,'jobSal'] = salary
    elif "年薪" in pay:
        salarytem = sal_df.at[j,'jobSal'].replace(',', '')  #以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*",salarytem)  #取出資料中的數值
        if len(salanum) == 1:  #若是1個數值即為薪資
            salary = int(salanum[0])
            salary = int(salary/12)
            sal_df.at[j,'jobSal'] = salary
        else:  #若是2個數值則取平均數
            salary = (int(salanum[0])+int(salanum[1]))/2
            salary = int(salary/12)
            sal_df.at[j,'jobSal'] = salary
    else:
        sal_df.at[j,'jobSal'] = None
        

job['jobSal'] = sal_df
job[['jobSal']] = job[['jobSal']].astype(float)


#  ===========================================================================

# 語文能力轉換為數字
language_df = job[['jobLanguage']]
for j in range(len(language_df)):
    fluent = language_df.at[j,'jobLanguage']
    if '精通' in fluent:
        language_df.at[j,'jobLanguage'] = 4
    elif'中等' in fluent:
        language_df.at[j,'jobLanguage'] = 3
    elif '略懂' in fluent:
        language_df.at[j,'jobLanguage'] = 2
    elif '不拘' in fluent:
        language_df.at[j,'jobLanguage'] = 1

job['LangTrans'] = language_df
job[['LangTrans']] = job[['LangTrans']].astype(float)
# 更改欄位的順序
columns_name = job.columns.tolist()
columns_name.insert(columns_name.index('jobLanguage')+1, 
                    columns_name.pop(columns_name.index('LangTrans')))
job = job[columns_name]



# job.to_excel('104data0712Transver1.xlsx', index=0)  #存為excel檔

