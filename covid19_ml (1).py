#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
import requests
import json


# In[2]:


path=r'C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe'
browser=webdriver.Chrome(executable_path=path)


# In[3]:


browser.get('https://data.covid19india.org/')


# In[4]:


data=browser.find_element_by_xpath('/html/body/div/table[1]/tbody/tr[1]/td[2]/a')


# In[5]:


data.click()


# In[6]:


time.sleep(10)


# In[7]:


r=requests.get('https://data.covid19india.org/v4/min/timeseries.min.json')


# In[8]:


column_name=['dates','total_confirmed']
Df=pd.DataFrame(columns=column_name)
Df


# In[9]:


for k in range(9):
    for i in range(9):
        try:
            Dat={}
            
            data1=json.loads(r.text)['KL']['dates']['2021-0{}-0{}'.format(k+1,i+1)]['total']['confirmed']
        #data1=json.loads(r.text)['KL']['dates']
        #print((data))
            Dat[Df.columns[0]]=['2021-0{}-0{}'.format(k+1,i+1)]
            Dat[Df.columns[1]]=data1
            Df=Df.append(Dat,ignore_index=True)
        
        except:
            continue
    for j in range(10):
        try:
            Dat2={}
            
            data2=json.loads(r.text)['KL']['dates']['2021-0{}-1{}'.format(k+1,j)]['total']['confirmed']
        #data1=json.loads(r.text)['KL']['dates']
        #print((data))
            Dat2[Df.columns[0]]=['2021-0{}-1{}'.format(k+1,j)]
            Dat2[Df.columns[1]]=data2
            Df=Df.append(Dat2,ignore_index=True)
        
        except:
            continue  
    for l in range(10):
        try:
            Dat3={}
            
            data3=json.loads(r.text)['KL']['dates']['2021-0{}-2{}'.format(k+1,l)]['total']['confirmed']
        #data1=json.loads(r.text)['KL']['dates']
        #print((data))
            Dat3[Df.columns[0]]=['2021-0{}-2{}'.format(k+1,l)]
            Dat3[Df.columns[1]]=data3
            Df=Df.append(Dat3,ignore_index=True)
        
        except:
            continue 
    
    for m in range(2):
        try:
            Dat4={}
            
            data4=json.loads(r.text)['KL']['dates']['2021-0{}-3{}'.format(k+1,m)]['total']['confirmed']
        #data1=json.loads(r.text)['KL']['dates']
        #print((data))
            Dat4[Df.columns[0]]=['2021-0{}-3{}'.format(k+1,m)]
            Dat4[Df.columns[1]]=data4
            Df=Df.append(Dat4,ignore_index=True)
        
        except:
            continue           


# In[12]:


display(Df)


# In[18]:


n_rows=Df.shape[0]


# In[19]:


pd.set_option('display.max_rows',n_rows)


# In[20]:


Df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




