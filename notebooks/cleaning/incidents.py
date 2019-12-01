#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


df = pd.read_csv('../../data/raw/Police_Department_Incident_Reports__Historical_2003_to_May_2018.csv')


# In[3]:


df


# In[4]:


df.rename(columns={'IncidntNum':'IncidentNum',
                   'Descript':'Description'},
          inplace=True)


# In[5]:


# df['Category'] = df['Category'].str.lower() 
# df['Description'] = df['Description'].str.lower() 
# df['DayOfWeek'] = df['DayOfWeek'].str.lower() 
# df['PdDistrict'] = df['PdDistrict'].str.lower() 
# df['Resolution'] = df['Resolution'].str.lower() 
# df['Address'] = df['Address'].str.lower() 
df = df.apply(lambda x: x.astype(str).str.lower())
df.head()


# In[6]:


df.dtypes


# In[7]:


df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y" )
df['Time'] = pd.to_datetime(df['Time'], format="%H:%M" ).dt.time


# In[8]:


df.dtypes


# In[9]:


df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


# In[10]:


df


# In[11]:


empty_sample = df[df.isnull().any(axis=1)]
print("Number of records contain 1+ null: ", empty_sample.shape[0], "\n")


# In[12]:


df.dropna(inplace=True)
empty_sample = df[df.isnull().any(axis=1)]
print("Number of records contain 1+ null: ", empty_sample.shape[0], "\n")


# In[13]:


df.dtypes


# In[ ]:


df.to_csv('../../data/processed/incidents.csv')

