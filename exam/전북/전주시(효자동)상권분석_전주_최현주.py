#!/usr/bin/env python
# coding: utf-8

# In[3]:


pd.Series(df.columns)


# In[40]:


import os,re
import pandas as pd
os.chdir(r'c:\doit\practice')

jeonju = pd.read_csv('전북상권분석.csv', encoding='cp949')

jeonju = jeonju[['시군구명', '상권업종대분류명', '상권업종중분류명', '위도', '경도']]
jeonju


# In[51]:


import pandas as pd

df = pd.read_csv('전북상권분석.csv', encoding='cp949')
df.head(3)


# In[57]:


import pandas as pd

df = pd.read_csv('전북상권분석.csv', encoding='cp949')

sub_df = df.loc[df['행정동명'].isin(['효자5동'])]

sub_df[['위도', '경도', '상호명']]


# In[1]:


import requests
import json

r = requests.get('https://raw.githubusercontent.com/southkorea/jeonju-maps/master/kostat/2013/json/_municipalities_geo_simple.json')

c = r.content

# 좌표 추출
jeonju_geo = json.loads
jeonju_geo


# In[69]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 30))

plt.rcParams['font.family'] = 'NanumGothic'

sns.countplot(y=jeonju['상권업종중분류명'], order=jeonju['상권업종중분류명'].value_counts().index)
plt.yticks(fontsize=12)
plt.title('전주시 업종별 개수')
plt.show()


# In[8]:


import folium
from folium.plugins import MarkerCluster
# 위도
latitude = 35.83217
# 경도
longitude = 127.1009

m = folium.Map(
    location=[latitude, longitude],
    zoom_start=15
)

coords = sub_df[['위도', '경도','상호명']]

marker_cluster = MarkerCluster().add_to(m)

for lat, long, point in zip(coords['위도'], coords['경도'],coords['상호명']):
    folium.Marker([lat, long], popup=point, icon = folium.Icon(color="green")).add_to(marker_cluster)

m


# In[ ]:




