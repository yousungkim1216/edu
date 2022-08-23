#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('전라북도_전기차충전소.csv', encoding='cp949')
df.head(3)


# In[3]:


df.info()


# In[4]:



# 위도
latitude = 35.425511
# 경도
longitude = 126.695163
m = folium.Map(location=[latitude, longitude],
zoom_start=17, 
width=750, 
height=500
)


# In[5]:


folium.Marker([latitude, longitude],
popup="고창지사",
tooltip="고창군").add_to(m)
m


# In[8]:


folium.CircleMarker([latitude, longitude],
color='tomato',
radius = 100, 
tooltip='고창군주변 권역').add_to(m)
m

