# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:41:15 2022

@author: user
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd



def get_job_data(keyword,page):
    while 1:
        try:
            job_data = []
            request_url = "https://www.104.com.tw/jobs/search/"
            query_str_params = {
                "ro":"1",
                "keyword":keyword,
                "order":"1",
                "sr":"99",
                "page":page,
                'jobexp': '5,10',
                "mode":"s",
                "jobsource":"2018indexpoc",
                "langFlag":"0",
                "langStatus":"0",
                "recommendJob":"1",
                "hotJob":"0"
                
            }
            
            USER_AGENT_LIST = [
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
                "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
                "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
                "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                ]
            USER_AGENT = random.choice(USER_AGENT_LIST)
            
            headers = {'user-agent': USER_AGENT}
            
            response = requests.get(request_url, params=query_str_params, headers=headers)
            soup = BeautifulSoup(response.text,'lxml')
            url = soup.select('.js-job-link')
            
            print(len(url))
            
            for i in range(0,len(url)-1):
                job_url = url[i].get('href')
                job_url = "https:" + job_url
                print(job_url)
            
                request_url = job_url
                response = requests.get(request_url)
                soup = BeautifulSoup(response.text,'lxml')
                
                # 標籤
                job_name = ".pr-6"
                job_edu = ".job-requirement-table .mb-2:nth-child(2) .mb-0"
                job_sal1 = ".align-top"
                job_sal2 = '.job-description-table .mb-2:nth-child(3) .mb-0'
                job_loc1 = ".job-address span"
                job_loc2 = '.job-description-table .mb-2:nth-child(5) .mb-0'
                job_exp = ".job-requirement-table .mb-2:nth-child(1) .mb-0"
                job_language1 = '.mb-0.w-100'
                job_language2 = ".t3.m-0"
                job_tool = ".tools u"
                job_business_trip = ".mb-2:nth-child(8) .mb-0"
                
                
                # 名稱爬取
                elements = soup.select(job_name)[0]
                job_name = elements.text.strip()
                
                
                # 學歷爬取
                elements = soup.select(job_edu)[0]
                job_edu = elements.text.strip()
                
                
                # 薪水爬取
                elements = soup.select(job_sal1)
                try:
                    if elements == []:
                        elements = soup.select(job_sal2)[0]
                        job_sal = elements.text.strip()
                    else:
                        job_sal = elements[0].text.strip()
                except IndexError:
                    job_sal = None
                
                # 地區爬取
                elements = soup.select(job_loc1)
                if elements == []:
                    elements = soup.select(job_loc2)[0].text.strip()
                    job_loc = elements
                    job_county = job_loc[:3]
                else:
                    job_loc = elements[0].text.strip()
                    job_county = job_loc[:3]
                
                # 經歷爬取
                elements = soup.select(job_exp)[0]
                job_exp = elements.text.strip()
                
                try:
                    if job_exp == "不拘":
                        job_exp = 0
                    else:
                        job_exp = int(job_exp[0])
                except ValueError:
                    job_exp = None
                
                # 使用工具的爬取
                tool_us = []
                elements = soup.select(job_tool)
                for i in range(len(elements)):
                    tool_us.append(elements[i].text)
                job_tool = tool_us
                job_tool_count = len(job_tool)
                
                # 語言能力的爬取
                elements = soup.select(job_language1)
                if elements == []:
                    elements = soup.select(job_language2)[0]
                    job_language = elements.text.strip()
                else:
                    job_language = elements[0].text.strip()
                
                # 外派爬取
                elements = soup.select(job_business_trip)[0]
                job_business_trip = elements.text.strip()
                
                software_job_data = {
                    'jobName': job_name,
                    'jobEdu': job_edu,
                    'jobSal': job_sal,
                    'jobLoc': job_loc,
                    'jobCounty':job_county,
                    'jobExp': job_exp,
                    'jobLanguage': job_language,
                    'jobKeyword': keyword,
                    'jobTool': job_tool,
                    'jobToolCount': job_tool_count,
                    'jobBusinessTrip': job_business_trip,
                    'jobUrl' : job_url
                    
                }
                
                t = random.randint(1,3)  # 隨機一個大於等於1且小於等於5的整數
                time.sleep(t)
                
                job_data.append(software_job_data)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
        return job_data


    
job_data_list = []
# jobMainTool = ['Java','Python','C#','C++',"JavaScript","PHP"]
jobMainTool = ['Java']
for i in range(len(jobMainTool)):
    for j in range(1):
        print(i,j)
        data = get_job_data(jobMainTool[i],j)
        job_data_list.append(data)
        
        
        
        
job_list = []
for i in range(len(job_data_list)):
    for j in range(len(job_data_list[i])):
        job_list.append(job_data_list[i][j])


job = pd.DataFrame(job_list)
job.to_excel('104jobdata0710.xlsx', index=0)  #存為excel檔