#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
import pandas as pd


# In[2]:


dataAll = requests.get("https://api.covid19india.org/v4/data-all.json").json()
newfile = open('neighbor-districts-modified.json')
neighbor_districts = json.load(newfile)


# In[3]:


date_exclude=['2020-01-30','2020-02-02','2020-02-03','2020-02-14','2020-03-02','2020-03-03','2020-03-04','2020-03-05','2020-03-06','2020-03-07',
          '2020-03-08','2020-03-09','2020-03-10','2020-03-11','2020-03-12','2020-03-13','2020-03-14','2020-09-06','2020-09-07',
          '2020-09-08','2020-09-09','2020-09-10','2020-09-11','2020-09-12','2020-09-13','2020-09-14','2020-09-15','2020-09-16',
          '2020-09-17','2020-09-18','2020-09-19','2020-09-20','2020-09-21']


# In[4]:


dataall=[]
for (key1,val1) in dataAll.items():
    if key1 not in date_exclude:
        for (key2,val2) in val1.items():
            if "districts" in val2.keys():
                for (key3,val3) in val2["districts"].items():
                    if 'delta' in val3.keys():
                        for (key4,val4) in val3['delta'].items():
                            if key4=='confirmed':
                                if(key2=='TG'):
                                    dataall.append((key1,key2,'telangana districts',val4))
                                elif(key2=='GA'):
                                    dataall.append((key1,key2,'goa districts',val4))
                                elif(key2=='AS'):
                                    dataall.append((key1,key2,'assam districts',val4))
                                elif(key2=='MN'):
                                    dataall.append((key1,key2,'manipur districts',val4))
                                elif(key2=='SK'):
                                    dataall.append((key1,key2,'sikkim districts',val4))
                                else:
                                    lo=key3.lower()
                                    dataall.append((key1,key2,lo,val4))


# In[5]:


dFrame=pd.DataFrame(dataall,columns=['date','statecode','district','cases'])


# In[6]:


map=pd.DataFrame(columns=['district','statecode','Q_id','dis_id'])
for key in neighbor_districts.keys():
    arr= key.split('_')
    map=map.append({'district':arr[0],'statecode':arr[1],'Q_id':arr[2],'dis_id':arr[3]},ignore_index=True)


# In[7]:


map.to_csv('mapping.csv',index=False)


# In[9]:


dtwise_cases=pd.merge(dFrame,map,how='left',on=['statecode','district'])


# In[10]:


dtwise_cases=dtwise_cases.drop('Q_id',axis=1)
dtwise_cases=dtwise_cases.dropna()


# In[11]:


dates=list(dtwise_cases['date'].unique())


# In[12]:


daycount=1
date_series={}
for date in dates:
    date_series[date]=daycount
    daycount+=1


# In[13]:


case_timeseries={}
for i in range(101,728):
    case_timeseries[i]={}
for i in range(101,728):
    for j in range(1,176):
        case_timeseries[i][j]=0
for ind,row in dtwise_cases.iterrows():
    case_timeseries[int(row['dis_id'])][date_series[row['date']]]=row['cases']


# In[14]:


cases_weekly=[]
for (key,val) in case_timeseries.items():
    totalcases=0
    weekcnt=1
    for i in range(1,176):
        totalcases+=val[i]
        if(i%7==0):
            cases_weekly.append((key,weekcnt,totalcases))
            weekcnt+=1
            totalcases=0


# In[15]:


cases_week=pd.DataFrame(cases_weekly,columns=['districtid','weekid','cases'])


# In[16]:


cases_week.to_csv('cases-week.csv',index=False)


# In[17]:


cases_monthly=[]
for (key,val) in case_timeseries.items():
    month=1
    totalcases=0
    for i in range(1,176):
        totalcases+=val[i]
        if (i==17 or i==47 or i==79 or i==108 or i==139 or i==170 or i==175):
            cases_monthly.append((key,month,totalcases))
            month+=1
            totalcases=0


# In[18]:


cases_month=pd.DataFrame(cases_monthly,columns=['districtid','monthid','cases'])
cases_month.to_csv('cases-month.csv',index=False)


# In[19]:


cases_overal=[]
i=-1
for did in range(101,728):
    totalcasesoverall=0
    for j in range(1,8):
        i+=1
        totalcasesoverall+=cases_monthly[i][2]
    cases_overal.append((did,1,totalcasesoverall))
cases_overall=pd.DataFrame(cases_overal,columns=['districtid','overallid','cases'])


# In[20]:


cases_overall.to_csv('cases-overall.csv',index=False)


# In[23]:


dic_week={}
for i in range(15675):
    dic_week[i]=int(cases_week.iloc[i]['cases'])


# In[24]:


with open("dic_week.json","w") as temp:
    json.dump(dic_week,temp)


# In[27]:


dic_month={}
for i in range(4389):
    dic_month[i]=int(cases_month.loc[i]['cases'])


# In[28]:


with open("dic_month.json","w") as temp:
    json.dump(dic_month,temp)


# In[29]:


dic_overall={}
for i in range(627):
    dic_overall[i]=int(cases_overall.loc[i]['cases'])


# In[30]:


with open("dic_overall.json","w") as temp:
    json.dump(dic_overall,temp)


# In[ ]:




