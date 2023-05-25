#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px
import re
from io import BytesIO
import requests
import json
from urllib.parse import urlencode
import gspread
import math as math
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
df=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q1_sample.csv')


# In[2]:


df['start_time']=pd.to_datetime(df.start_time)
df['end_time']=pd.to_datetime(df.end_time)
df=df.set_index(df.start_time)


# In[7]:


dfap=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q2_sample_apr.csv')
dfma=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q2_sample_may.csv')
dfjun=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q2_sample_jun.csv')
dfjul=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q3_sample_july.csv')
dfau=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q3_sample_aug.csv')
dfsep=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q3_sample_sep.csv')
dfoct=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q4_sample_oct.csv')
dfnov=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q4_sample_nov.csv')
dfdec=pd.read_csv('/mnt/HC_Volume_18315164/home-jupyter/jupyter-a-/lesson_8/bikes_q4_sample_dec.csv')


# In[8]:


bikes = pd.concat([dfap,dfma,dfjun, dfjul,dfau,dfsep,dfoct,dfnov,dfdec])


# In[9]:


bikes


# In[10]:


bikes['start_time']=pd.to_datetime(bikes['start_time'])
bikes['end_time']=pd.to_datetime(bikes['end_time'])
bikes=bikes.set_index(bikes.start_time)


# In[11]:


bikes.dtypes


# In[17]:


# сохраним наблюдения с 1 июня по 31 августа
bikes_summer = bikes.loc['2018-06-01' : '2018-08-31']
bikes_summer


# In[18]:


# Найдем наиболее популярный пункт назначения
top_destination = bikes_summer.groupby('to_station_name').agg({'trip_id':'count'}).sort_values('trip_id', ascending = False)
top_destination


# In[19]:


top_destination =bikes_summer.to_station_name.value_counts().idxmax()
top_destination


# In[20]:


# определим в какой день в полученный пункт было совершено меньше всего поездок
bad_day = bikes_summer.query('to_station_name == @top_destination').resample('D').size().idxmin().strftime('%Y-%m-%d')
bad_day


# In[40]:


df


# In[45]:


df.style.hide_index()


# In[ ]:




