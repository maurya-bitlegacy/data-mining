#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[2]:


week_nbrs=pd.read_csv('neighbor-week.csv')


# In[3]:


week_state = pd.read_csv('state-week.csv')


# In[4]:


cases_week = pd.read_csv('cases-week.csv')


# In[5]:


distid=[]
weekid=[]
nzscore=[]
szscore=[]
for i in range(0,15675):
    nbr_data = week_nbrs.loc[i]
    state_data = week_state.loc[i]
    self_data = cases_week.loc[i]
    nbrzscore = round((self_data['cases']-nbr_data['neighbormean'])/nbr_data['neighborstdev'],2)
    statezscore = round((self_data['cases']-state_data['statemean'])/state_data['statestdev'],2)
    distid.append(self_data['districtid'])
    weekid.append(self_data['weekid'])
    nzscore.append(nbrzscore)
    szscore.append(statezscore)
newdf = pd.DataFrame(list(zip(distid,weekid,nzscore,szscore)), columns =['districtid','weekid','neighborhoodzscore','statezscore']) 


# In[6]:


newdf=newdf.replace([np.inf, -np.inf], np.nan)
newdf.fillna(0,inplace=True)


# In[7]:


month_nbrs=pd.read_csv('neighbor-month.csv')


# In[8]:


month_state = pd.read_csv('state-month.csv')


# In[9]:


cases_month = pd.read_csv('cases-month.csv')


# In[10]:


distid=[]
monthid=[]
nzscore=[]
szscore=[]
for i in range(0,4389):
    nbr_data = month_nbrs.loc[i]
    state_data = month_state.loc[i]
    self_data = cases_month.loc[i]
    nbrzscore = round((self_data['cases']-nbr_data['neighbormean'])/nbr_data['neighborstdev'],2)
    statezscore = round((self_data['cases']-state_data['statemean'])/state_data['statestdev'],2)
    distid.append(self_data['districtid'])
    monthid.append(self_data['monthid'])
    nzscore.append(nbrzscore)
    szscore.append(statezscore)
newdf1 = pd.DataFrame(list(zip(distid,monthid,nzscore,szscore)), columns =['districtid','monthid','neighborhoodzscore','statezscore']) 


# In[11]:


newdf1=newdf1.replace([np.inf, -np.inf], np.nan)
newdf1.fillna(0,inplace=True)


# In[12]:


overall_nbrs=pd.read_csv('neighbor-overall.csv')


# In[13]:


overall_state = pd.read_csv('state-overall.csv')


# In[14]:


cases_overall = pd.read_csv('cases-overall.csv')


# In[15]:


distid=[]
overallid=[]
nzscore=[]
szscore=[]
for i in range(0,627):
    nbr_data = overall_nbrs.loc[i]
    state_data = overall_state.loc[i]
    self_data = cases_overall.loc[i]
    nbrzscore = round((self_data['cases']-nbr_data['neighbormean'])/nbr_data['neighborstdev'],2)
    statezscore = round((self_data['cases']-state_data['statemean'])/state_data['statestdev'],2)
    distid.append(self_data['districtid'])
    overallid.append(self_data['overallid'])
    nzscore.append(nbrzscore)
    szscore.append(statezscore)
newdf2=pd.DataFrame(list(zip(distid,overallid,nzscore,szscore)), columns =['districtid','overallid','neighborhoodzscore','statezscore']) 


# In[16]:


newdf2=newdf2.replace([np.inf, -np.inf], np.nan)
newdf2.fillna(0,inplace=True)


# In[17]:


newdf.to_csv("zscore-week.csv",index=False)
newdf1.to_csv("zscore-month.csv",index=False)
newdf2.to_csv("zscore-overall.csv",index=False)

