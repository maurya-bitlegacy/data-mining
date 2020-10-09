#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import json
import datetime
import statistics


# In[2]:


zweek = pd.read_csv("zscore-week.csv")
zmonth = pd.read_csv("zscore-month.csv")
zoverall = pd.read_csv("zscore-overall.csv")


# In[3]:


zweek_sortedn=zweek.sort_values(['weekid','neighborhoodzscore'],ascending=[True, False])
zweek_sortedn.reset_index(drop=True,inplace=True)


# In[4]:


zweek_sorteds=zweek.sort_values(['weekid','statezscore'],ascending=[True, False])
zweek_sorteds.reset_index(drop=True,inplace=True)


# In[5]:


newdf = pd.DataFrame(columns=['weekid','method','spot','district1','district2','district3','district4','district5'])
index=0
while(index<15675):
    dishotn=[]
    discoldn=[]
    dishots=[]
    discolds=[]
    subdfhotn = zweek_sortedn[index:index+627].head(5)
    subdfcoldn = zweek_sortedn[index+622:index+627]
    subdfhots = zweek_sorteds[index:index+627].head(5)
    subdfcolds = zweek_sorteds[index+622:index+627]
    week = str(int(subdfhotn.iloc[0]['weekid']))
    dishotn=list(subdfhotn['districtid'])
    discoldn=list(subdfcoldn['districtid'])
    dishots=list(subdfhots['districtid'])
    discolds=list(subdfcolds['districtid'])
    newdf=newdf.append({'weekid':week,'method':'neighborhood','spot': 'hot','district1':dishotn[0],'district2':dishotn[1],'district3':dishotn[2],'district4':dishotn[3],'district5':dishotn[4]},ignore_index=True)
    newdf=newdf.append({'weekid':week,'method':'neighborhood','spot': 'cold','district1':discoldn[0],'district2':discoldn[1],'district3':discoldn[2],'district4':discoldn[3],'district5':discoldn[4]},ignore_index=True)  
    newdf=newdf.append({'weekid':week,'method':'state','spot': 'hot','district1':dishots[0],'district2':dishots[1],'district3':dishots[2],'district4':dishots[3],'district5':dishots[4]},ignore_index=True)
    newdf=newdf.append({'weekid':week,'method':'state','spot': 'cold','district1':discolds[0],'district2':discolds[1],'district3':discolds[2],'district4':discolds[3],'district5':discolds[4]},ignore_index=True)  
    index+=627


# In[6]:


zmonth_sortedn=zmonth.sort_values(['monthid','neighborhoodzscore'],ascending=[True, False])
zmonth_sortedn.reset_index(drop=True,inplace=True)
zmonth_sorteds=zmonth.sort_values(['monthid','statezscore'],ascending=[True, False])
zmonth_sorteds.reset_index(drop=True,inplace=True)


# In[7]:


newdf1 = pd.DataFrame(columns=['monthid','method','spot','district1','district2','district3','district4','district5'])
index=0
while(index<4389):
    dishots=[]
    discolds=[]
    dishotn=[]
    discoldn=[]
    subdfhotn = zmonth_sortedn[index:index+627].head(5)
    subdfcoldn = zmonth_sortedn[index+622:index+627]
    subdfhots = zmonth_sorteds[index:index+627].head(5)
    subdfcolds = zmonth_sorteds[index+622:index+627]
    month = str(int(subdfhotn.iloc[0]['monthid']))
    dishotn=list(subdfhotn['districtid'])
    discoldn=list(subdfcoldn['districtid'])
    dishots=list(subdfhots['districtid'])
    discolds=list(subdfcolds['districtid'])
    newdf1=newdf1.append({'monthid':month,'method':'neighborhood','spot': 'hot','district1':dishotn[0],'district2':dishotn[1],'district3':dishotn[2],'district4':dishotn[3],'district5':dishotn[4]},ignore_index=True)
    newdf1=newdf1.append({'monthid':month,'method':'neighborhood','spot': 'cold','district1':discoldn[0],'district2':discoldn[1],'district3':discoldn[2],'district4':discoldn[3],'district5':discoldn[4]},ignore_index=True)  
    newdf1=newdf1.append({'monthid':month,'method':'state','spot': 'hot','district1':dishots[0],'district2':dishots[1],'district3':dishots[2],'district4':dishots[3],'district5':dishots[4]},ignore_index=True)
    newdf1=newdf1.append({'monthid':month,'method':'state','spot': 'cold','district1':discolds[0],'district2':discolds[1],'district3':discolds[2],'district4':discolds[3],'district5':discolds[4]},ignore_index=True)  
    index+=627


# In[8]:


zoverall_sortedn=zoverall.sort_values(['neighborhoodzscore'],ascending=[False])
zoverall_sortedn.reset_index(drop=True,inplace=True)
zoverall_sorteds=zoverall.sort_values(['statezscore'],ascending=[False])
zoverall_sorteds.reset_index(drop=True,inplace=True)


# In[9]:


newdf2 = pd.DataFrame(columns=['overallid','method','spot','district1','district2','district3','district4','district5'])
index=0
dishotn=[]
discoldn=[]
dishots=[]
discolds=[]
subdfhotn = zoverall_sortedn[0:5]
subdfcoldn = zoverall_sortedn[622:627]
subdfhots = zoverall_sorteds[0:5]
subdfcolds = zoverall_sorteds[622:627]
dishotn=list(subdfhotn['districtid'])
discoldn=list(subdfcoldn['districtid'])
dishots=list(subdfhots['districtid'])
discolds=list(subdfcolds['districtid'])
newdf2=newdf2.append({'overallid':'1','method':'neighborhood','spot': 'hot','district1':dishotn[0],'district2':dishotn[1],'district3':dishotn[2],'district4':dishotn[3],'district5':dishotn[4]},ignore_index=True)
newdf2=newdf2.append({'overallid':'1','method':'neighborhood','spot': 'cold','district1':discoldn[0],'district2':discoldn[1],'district3':discoldn[2],'district4':discoldn[3],'district5':discoldn[4]},ignore_index=True)
newdf2=newdf2.append({'overallid':'1','method':'state','spot': 'hot','district1':dishots[0],'district2':dishots[1],'district3':dishots[2],'district4':dishots[3],'district5':dishots[4]},ignore_index=True)
newdf2=newdf2.append({'overallid':'1','method':'state','spot': 'cold','district1':discolds[0],'district2':discolds[1],'district3':discolds[2],'district4':discolds[3],'district5':discolds[4]},ignore_index=True)  


# In[10]:


newdf.to_csv("top-week.csv",index=False)
newdf1.to_csv("top-month.csv",index=False)
newdf2.to_csv("top-overall.csv",index=False)


# In[ ]:




