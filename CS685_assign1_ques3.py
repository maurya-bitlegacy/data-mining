#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json
import math


# In[2]:


tempfile = open('neighbor-districts-modified.json') # Contains the neighbors of each district
nbrs = json.load(tempfile)


# In[3]:


maps=pd.read_csv('mapping.csv')


# In[4]:


dic_nbrs={}
for i in range(101,728):
    dic_nbrs[i]={}
distid=101
for (key,value) in nbrs.items():
    listindex=0
    for val in value:
        nbrid=maps[(maps['district']==val.split('/')[0]) & (maps['Q_id']==val.split('/')[1])]['dis_id'].unique()[0]
        dic_nbrs[distid][listindex]=str(nbrid)
        listindex+=1
    distid+=1


# In[5]:


und_graph=pd.DataFrame(columns=['district_id','neighbor_id'])
for (key1,val1) in dic_nbrs.items():
    for (key2,val2) in val1.items():
        und_graph=und_graph.append({'district_id':key1,'neighbor_id':val2},ignore_index=True)


# In[6]:


with open("district_neighbors.json","w") as temp:
    json.dump(dic_nbrs,temp)
und_graph.to_csv("edge-graph.csv",index=False)


# In[ ]:




