#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install folium


# In[2]:


import folium


# In[ ]:


import pandas as pd

df=pd.read_csv('소상공인시장진흥공단_상가(상권)정보_전북_202206.csv',encoding='utf8')
sub_df=df.loc[df['행정동명'].isin(['평화1동','평화2동'])]
sub_df[['상호명','도로명주소','위도','경도']]


# In[4]:


from folium.plugins import MarkerCluster


# In[ ]:


m=folium.Map(location=[latitude, longitude], zoom_start=15, width=850, height=600)
coords=sub_df[['위도', '경도']]

marker_cluster=MarkerCluster().add_to(m)
for lat, long in zip (coords['위도'], coords['경도']):
    folium.Marker([lat, long], icon=folium.Icon(color='blue')).add_to(marker_cluster)
m


# In[ ]:




