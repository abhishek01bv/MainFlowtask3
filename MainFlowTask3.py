#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[2]:


df = pd.read_csv('householdtask3.csv')


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


plt.scatter(df['year'], df['own'])
plt.title('scatter plot')
plt.xlabel('year')
plt.ylabel('own')


# In[6]:


plt.plot(df['year'])
plt.plot(df['own'])
plt.title('Line chart')
plt.xlabel('year')
plt.ylabel('own')


# In[7]:


plt.bar(df['year'], df['own'])
plt.title('scatter plot')
plt.xlabel('year')
plt.ylabel('own')


# In[9]:


plt.hist(df['income'])
plt.title('Histogram')


# In[ ]:




