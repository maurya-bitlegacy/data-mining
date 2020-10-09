#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import math
import numpy as np
import statistics


# In[2]:


mappings=pd.read_csv('mapping.csv')


# In[3]:


dic_states={}
for index,row in mappings.iterrows():
    if dic_states.get(row['statecode'])==None:
        dic_states[row['statecode']] = [row['dis_id']]
    else:
        dic_states[row['statecode']] += [row['dis_id']] 


# In[4]:


week_timeseries = pd.read_csv('cases-week.csv')


# In[5]:


file1 = open('dic_week.json') # Contains the neighbors of each district
dic_week = json.load(file1)
file2 = open('dic_month.json') # Contains the neighbors of each district
dic_month = json.load(file2)
file3 = open('dic_overall.json') # Contains the neighbors of each district
dic_overall = json.load(file3)


# In[6]:


dist=[]
weekk=[]
meann=[]
stdevv=[]
for curdist in range(101,728):
    flag=0
    for state,districts in dic_states.items():
        for district in districts:
            if district ==curdist:
                otherdistricts = districts[:]
                otherdistricts.remove(district)
                for week in range(1,26):
                    mean=0
                    stdev=0
                    dist_cases=[]
                    for otherdistrict in otherdistricts:
                        dist_cases.append(dic_week[str((int(otherdistrict)-101)*25+week-1)])
                    if len(dist_cases)<1:
                        mean=0
                        stdev=0
                    elif len(dist_cases)<2:
                        mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                        stdev=0
                    else:
                        mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                        stdev = round((statistics.stdev(dist_cases)),2)
                    dist.append(curdist)
                    weekk.append(week)
                    meann.append(mean)
                    stdevv.append(stdev)
                flag=1
                break
        if flag==1:
            break
newdf = pd.DataFrame(list(zip(dist,weekk,meann,stdevv)), columns =['districtid','weekid','statemean','statestdev'])                 
                    
                
                            


# In[8]:


newdf.to_csv("state-week.csv",index=False)


# In[9]:


month_timeseries = pd.read_csv('cases-month.csv')


# In[10]:


dist=[]
monthh=[]
meann=[]
stdevv=[]
for curdist in range(101,728):
    flag=0
    for state,districts in dic_states.items():
        for district in districts:
            if district ==curdist:
                otherdistricts = districts[:]
                otherdistricts.remove(district)
                for month in range(1,8):
                    mean=0
                    stdev=0
                    dist_cases=[]
                    for otherdistrict in otherdistricts:
                        dist_cases.append(dic_month[str((int(otherdistrict)-101)*7+month-1)])
                    if len(dist_cases)<1:
                        mean=0
                        stdev=0
                    elif len(dist_cases)<2:
                        mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                        stdev=0
                    else:
                        mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                        stdev = round((statistics.stdev(dist_cases)),2)
                    dist.append(curdist)
                    monthh.append(month)
                    meann.append(mean)
                    stdevv.append(stdev)
                flag=1
                break
        if flag==1:
            break
newdf1 = pd.DataFrame(list(zip(dist,monthh,meann,stdevv)), columns =['districtid','monthid','statemean','statestdev'])                 


# In[12]:


newdf1.to_csv("state-month.csv",index=False)


# In[13]:


overall_timeseries = pd.read_csv('cases-overall.csv')


# In[14]:


newdf2 = pd.DataFrame(columns=['districtid','overallid','statemean','statestdev'])
dist=[]
meann=[]
stdevv=[]
ones=[]
for curdist in range(101,728):
    for state,districts in dic_states.items():
        for district in districts:
            if district ==curdist:
                otherdistricts = districts[:]
                otherdistricts.remove(district)
                mean=0
                stdev=0
                dist_cases=[]
                for otherdistrict in otherdistricts:
                    dist_cases.append(dic_overall[str(int(otherdistrict)-101)])
                if len(dist_cases)<1:
                    mean=0
                    stdev=0
                elif len(dist_cases)<2:
                    mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                    stdev=0
                else:
                    mean = round((np.sum(dist_cases)/len(dist_cases)),2)
                    stdev = round((statistics.stdev(dist_cases)),2)
                dist.append(curdist)
                meann.append(mean)
                stdevv.append(stdev)
                ones.append(1)
newdf2 = pd.DataFrame(list(zip(dist,ones,meann,stdevv)), columns =['districtid','overallid','statemean','statestdev'])                 
               


# In[16]:


newdf2.to_csv("state-overall.csv",index=False)


# In[ ]:




