#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os,re


# In[3]:


os.chdir(r'C:\doit')


# In[5]:


import usecsv


# In[29]:


apt = usecsv.switch(usecsv.opencsv('apt_2022.csv'))


# In[52]:


for i in apt:
    try:
        if i[5] >= 100 and i[8] <=50000 and re.match('부산',i[0]):
            print(i[0],i[5],i[8])
    except: pass


# In[ ]:




