#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import statistics


# In[2]:


temp = open('district_neighbors.json') # Contains the neighbors of each district
neighbor_list = json.load(temp)


# In[3]:


cases_week=pd.read_csv('cases-week.csv')


# In[4]:


file1 = open('dic_week.json') # Contains the neighbors of each district
dic_week = json.load(file1)


# In[5]:


lis_dist=[]
lis_mean=[]
lis_stdev=[]
lis_week=[]
mean=0
stdev=0
for (district,neighbors) in neighbor_list.items():
    for i in range(1,26):
        l=[]
        for (k2,neighbor) in neighbors.items():
            l.append(dic_week[str((int(neighbor)-101)*25+i-1)])
        if(len(l)==0):
            mean=0
            stdev=0
       
        if(len(l)<2):
            mean=l[0]
            stdev=0
        else:
            mean= round(np.mean(l),2)
            stdev=round(statistics.stdev(l),2)
        lis_dist.append(district)
        lis_mean.append(mean)
        lis_stdev.append(stdev)
        lis_week.append(i)
mean_week=pd.DataFrame(list(zip(lis_dist,lis_week,lis_mean,lis_stdev)), columns =['districtid', 'weekid', 'neighbormean', 'neighborstdev'])                 


# In[6]:


cases_month=pd.read_csv('cases-month.csv')
tempfile = open('dic_month.json')
dic_month = json.load(tempfile)


# In[7]:


lis_dist=[]
lis_mean=[]
lis_stdev=[]
lis_month=[]
mean=0
stdev=0
for(district,neighbors) in neighbor_list.items():
    for i in range(1,8):
        neighbor_month=[]
        for (k2,neighbor) in neighbors.items():
            neighbor_month.append(dic_month[str((int(neighbor)-101)*7+i-1)])
        if(len(neighbor_month)==0):
            mean=0
            stdev=0
        elif(len(neighbor_month)<2):
            mean=neighbor_month[0]
            stdev=0
        else:
            mean=round(np.mean(neighbor_month),2)
            stdev=round(statistics.stdev(neighbor_month,mean),2)
        lis_dist.append(district)
        lis_mean.append(mean)
        lis_stdev.append(stdev)
        lis_month.append(i)
mean_month=pd.DataFrame(list(zip(lis_dist,lis_month,lis_mean,lis_stdev)), columns =['districtid', 'monthid', 'neighbormean', 'neighborstdev'])                 


# In[8]:


cases_overall=pd.read_csv('cases-overall.csv')
file1 = open('dic_overall.json') # Contains the neighbors of each district
dic_overall = json.load(file1)


# In[9]:


mean_overall=pd.DataFrame(columns=['districtid', 'overallid', 'neighbormean', 'neighborstdev'])
mean=0
stdev=0
for(district,neighbors) in neighbor_list.items():
    neighbor_overall=[]
    for (k2,neighbor) in neighbors.items():
        neighbor_overall.append(dic_overall[str(int(neighbor)-101)])
    if len(neighbor_overall)==0:
        mean=0
        stdev=0
    elif(len(neighbor_overall)<2):
        mean=neighbor_month[0]
        stdev=0
    else:
        mean=round(np.mean(neighbor_overall),2)
        stdev=round(statistics.stdev(neighbor_overall,mean),2)
    mean_overall=mean_overall.append({'districtid':str(district),'overallid':str(1),'neighbormean':mean,'neighborstdev':stdev},ignore_index=True)


# In[10]:


mean_week.to_csv('neighbor-week.csv',index=False)


# In[11]:


mean_month.to_csv('neighbor-month.csv',index=False)


# In[12]:


mean_overall.to_csv('neighbor-overall.csv',index=False)

