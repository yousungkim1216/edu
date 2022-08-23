#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install folium


# In[7]:


import folium


# In[11]:


import folium


# In[21]:


import glob
files = glob.glob('*불법주정차*')
files

gangdong=files[0]
pd.read_csv(gangdong, encoding='cp949')
pd.read_csv(gangdong, encoding='cp949').dtypes


# In[22]:


df_list = []
for file in files:
    try:
        raw = pd.read_csv(file, encoding='cp949')
        df_list.append(raw)
    except:
        raw = pd.read_csv(file, encoding='utf-8')
        df_list.append(raw)
        
df_list


# In[24]:


df = pd.concat(df_list)
df


# In[26]:


df.reset_index(drop=True, inplace = True)
df
df.info()


# In[27]:


df.isnull().sum(0)


# In[28]:


import folium

# 위도
latitude = 37.553664
# 경도
longitude = 126.9653595

m3 = folium.Map(
    location=[latitude, longitude],
    zoom_start=15
)

m3

from folium.plugins import MarkerCluster

marker_cluster = MarkerCluster().add_to(m3)

for lat, lng, name in zip(df['위도'], df['경도'], df['단속지점명']):
    folium.Marker([lat,lng], icon = folium.Icon(icon='camera', color='red'), popup = f'<pre>{name}</pre>').add_to(marker_cluster)

m3


# In[ ]:




