#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install folium


# In[ ]:


import folium


# In[ ]:


latitude=35.785713
longitude=127.129041
m=folium.Map(location=[latitude, longitude], zoom_start=17, width=850, height=600)
folium.Marker([latitude, longitude],
    popup="와이식자재 모악로점",
    tooltip="고객과 함께 하는 와이식자재-24시간 운영",
    icon=folium.Icon('red')).add_to(m)
folium.CircleMarker([latitude, longitude], color='orange', radius=50, tooltip="평화동 식자재마트").add_to(m)
m


# In[ ]:




