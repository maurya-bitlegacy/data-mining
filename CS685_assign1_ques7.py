#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[2]:


neighbor_week = pd.read_csv("neighbor-week.csv")
neighbor_month = pd.read_csv("neighbor-month.csv")
neighbor_overall = pd.read_csv("neighbor-overall.csv")
state_week = pd.read_csv("state-week.csv")
state_month = pd.read_csv("state-month.csv")
state_overall = pd.read_csv("state-overall.csv")


# In[3]:


file1 = open('dic_week.json') # Contains the neighbors of each district
dic_week = json.load(file1)
file2 = open('dic_month.json') # Contains the neighbors of each district
dic_month = json.load(file2)
file3 = open('dic_overall.json') # Contains the neighbors of each district
dic_overall = json.load(file3)


# In[4]:


dic_nmeanweek={}
for i in range(15675):
    dic_nmeanweek[i]=neighbor_week.iloc[i]['neighbormean']
dic_nmeanmonth={}
for i in range(4389):
    dic_nmeanmonth[i]=neighbor_month.iloc[i]['neighbormean']
dic_nmeanoverall={}
for i in range(627):
    dic_nmeanoverall[i]=neighbor_overall.iloc[i]['neighbormean']


# In[5]:


dic_nstdweek={}
for i in range(15675):
    dic_nstdweek[i]=neighbor_week.iloc[i]['neighborstdev']
dic_nstdmonth={}
for i in range(4389):
    dic_nstdmonth[i]=neighbor_month.iloc[i]['neighborstdev']
dic_nstdoverall={}
for i in range(627):
    dic_nstdoverall[i]=neighbor_overall.iloc[i]['neighborstdev']


# In[6]:


dic_smeanweek={}
for i in range(15675):
    dic_smeanweek[i]=state_week.iloc[i]['statemean']
dic_smeanmonth={}
for i in range(4389):
    dic_smeanmonth[i]=state_month.iloc[i]['statemean']
dic_smeanoverall={}
for i in range(627):
    dic_smeanoverall[i]=state_overall.iloc[i]['statemean']


# In[7]:


dic_sstdweek={}
for i in range(15675):
    dic_sstdweek[i]=state_week.iloc[i]['statestdev']
dic_sstdmonth={}
for i in range(4389):
    dic_sstdmonth[i]=state_month.iloc[i]['statestdev']
dic_sstdoverall={}
for i in range(627):
    dic_sstdoverall[i]=state_overall.iloc[i]['statestdev']


# In[8]:


weeks =[]
methodd=[]
spott=[]
did=[]
for weekid in range(1,26):
    spot=""
    currentindex = weekid-1
    while(currentindex<15675):
        cases = dic_week[str(currentindex)]
        mean = dic_nmeanweek[currentindex]
        stdev = dic_nstdweek[currentindex]
        disid = (currentindex-weekid+1)//25 + 101
        if cases>(mean+stdev):
            spot = "hot"
        else:
            spot = "cold"
        weeks.append(weekid)
        methodd.append("neighborhood")
        spott.append(spot)
        did.append(disid)
        currentindex +=25
ndf1 = pd.DataFrame(list(zip(weeks,methodd,spott,did)), columns =['weekid','method','spot','districtid'])                 


# In[9]:


monthh=[]
methodd=[]
spott=[]
did=[]
for monthid in range(1,8):
    spot=""
    currentindex = monthid-1
    while(currentindex<4389):
        cases = dic_month[str(currentindex)]
        mean = dic_nmeanmonth[currentindex]
        stdev = dic_nstdmonth[currentindex]
        disid = (currentindex-monthid+1)//7 + 101
        if cases>(mean+stdev):
            spot = "hot"
        else:
            spot = "cold"
        monthh.append(monthid)
        methodd.append("neighborhood")
        spott.append(spot)
        did.append(disid)
        currentindex +=7
ndf2 = pd.DataFrame(list(zip(monthh,methodd,spott,did)), columns =['monthid','method','spot','districtid'])                 


# In[10]:


overalll=[]
methodd=[]
spott=[]
did=[]
for disid in range(101,728):
    cases = dic_overall[str(disid-101)]
    mean = dic_nmeanoverall[disid-101]
    stdev = dic_nstdoverall[disid-101]
    if cases>(mean+stdev):
        spot = "hot"
    else:
        spot = "cold"
    overalll.append(1)
    methodd.append("neighborhood")
    spott.append(spot)
    did.append(disid)
ndf3 = pd.DataFrame(list(zip(overalll,methodd,spott,did)), columns =['overallid','method','spot','districtid'])                 


# In[11]:


ndf1.to_csv('neighborhood-spot-week.csv',index=False)
ndf2.to_csv('neighborhood-spot-month.csv',index=False)
ndf3.to_csv('neighborhood-spot-overall.csv',index=False)


# In[12]:


weeks =[]
methodd=[]
spott=[]
did=[]
for weekid in range(1,26):
    spot=""
    currentindex = weekid-1
    while(currentindex<15675):
        cases = dic_week[str(currentindex)]
        mean = dic_smeanweek[currentindex]
        stdev = dic_sstdweek[currentindex]
        disid = (currentindex-weekid+1)//25 + 101
        if cases>(mean+stdev):
            spot = "hot"
        else:
            spot = "cold"
        weeks.append(weekid)
        methodd.append("state")
        spott.append(spot)
        did.append(disid)
        currentindex +=25
ndf4 = pd.DataFrame(list(zip(weeks,methodd,spott,did)), columns =['weekid','method','spot','districtid'])                 


# In[13]:


monthh=[]
methodd=[]
spott=[]
did=[]
for monthid in range(1,8):
    spot=""
    currentindex = monthid-1
    while(currentindex<4389):
        cases = dic_month[str(currentindex)]
        mean = dic_smeanmonth[currentindex]
        stdev = dic_sstdmonth[currentindex]
        disid = (currentindex-monthid+1)//7 + 101
        if cases>(mean+stdev):
            spot = "hot"
        else:
            spot = "cold"
        monthh.append(monthid)
        methodd.append("state")
        spott.append(spot)
        did.append(disid)
        currentindex +=7
ndf5 = pd.DataFrame(list(zip(monthh,methodd,spott,did)), columns =['monthid','method','spot','districtid'])                 


# In[14]:


ndf6 = pd.DataFrame(columns=['overallid','method','spot','districtid'])
overalll=[]
methodd=[]
spott=[]
did=[]
for disid in range(101,728):
    cases = dic_overall[str(disid-101)]
    mean = dic_smeanoverall[disid-101]
    stdev = dic_sstdoverall[disid-101]
    if cases>(mean+stdev):
        spot = "hot"
    else:
        spot = "cold"
    overalll.append(1)
    methodd.append("state")
    spott.append(spot)
    did.append(disid)
ndf6 = pd.DataFrame(list(zip(overalll,methodd,spott,did)), columns =['overallid','method','spot','districtid'])                 


# In[15]:


ndf4.to_csv('state-spot-week.csv',index=False)
ndf5.to_csv('state-spot-month.csv',index=False)
ndf6.to_csv('state-spot-overall.csv',index=False)


# In[ ]:




