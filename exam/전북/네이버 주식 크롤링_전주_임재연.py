#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"


# In[2]:


req = requests.get(url)
# html 정보에서 text정보만 추출
html = req.text
soup = BeautifulSoup(html, 'html.parser')


# In[3]:


# my_stock 변수에 select 할 내용을 찾아서 넣어준다
my_stock = soup.select('.lst_pop')

for stock_name in my_stock:
    print(stock_name.text)


# In[4]:


# my_stock 변수에 select 할 내용을 찾아서 넣어준다
my_stock = soup.select('.lst_major')


for stock_name in my_stock:
    print(stock_name.text)


# In[5]:


import urllib.request

# 웹사이트 정보 요청
page = urllib.request.urlopen(url)

# 해당 페이지는 cp949 방식의 인코딩 사용
html = page.read().decode('cp949')

soup = BeautifulSoup(html, 'html.parser')

soup.select('span.num')


# In[6]:


soup.select('span.num')[1]
soup.select('span.num')[1].string
float(soup.select('span.num')[1].string.replace(',', ''))


# In[7]:


# input으로 id = 'KOSPI_now' 처럼 지정
soup.find(id = 'KOSPI_now')
# string 속성을 가져와 원하는 데이터까지 도달
soup.find(id = 'KOSPI_now').string


# In[8]:


# 코스피 등락률 크롤링
soup.find(id = 'KOSPI_change')

soup.find(id = 'KOSPI_change').contents

soup.find(id = 'KOSPI_change').contents[2]

soup.find(id = 'KOSPI_change').contents[2].split()

soup.find(id = 'KOSPI_change').contents[3].string


# In[17]:


import pandas as pd
import requests
code = '323410'
URL = f"https://finance.naver.com/item/main.nhn?code={code}"
r = requests.get(URL)
df = pd.read_html(r.text)[3]
df


# In[18]:


import pandas as pd
import requests
code = '005930'
URL = f"https://finance.naver.com/item/main.nhn?code={code}"
r = requests.get(URL)
df = pd.read_html(r.text)[3]
df.set_index(df.columns[0],inplace=True)
df.index.rename('주요재무정보', inplace=True)
df.columns = df.columns.droplevel(2)
annual_date = pd.DataFrame(df).xs('최근 연간 실적',axis=1)
quater_date = pd.DataFrame(df).xs('최근 분기 실적',axis=1)


# In[19]:


def return_value(address):
    res = requests.get(address)
    soup = BeautifulSoup(res.content, 'html.parser')

    section = soup.find('tbody')
    items = section.find_all('tr', onmouseover="mouseOver(this)")
    for item in items:
        basic_info = item.get_text()
        sinfo = basic_info.split("\n")
        print("\t" + sinfo[1] + "\t\t" + sinfo[2] + "\t\t\t" + sinfo[3])


baseaddress = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
for i in range(1,35):
    return_value(baseaddress+str(i))


# In[20]:


pip install finance-datareader


# In[22]:


import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')

# 개별 종목 가격 데이터 가져오기
#df = fdr.DataReader('종목코드', '시작일자'. '종료일자')

# 한국주식 (삼성전자)
df = fdr.DataReader('005930', '2022')

# 미국주식 (APPLE) # df['Close'].plot();
df = fdr.DataReader('AAPL', '2022')

# ETF 데이터 가져오기 # 미국(ETF/US), 일본(ETF/JP)
df_etf = fdr.StockListing('ETF/KR')
df_etf

# KODEX 200선물인버스2X 사례
df_inver = fdr.DataReader('252670')
df_inver


# In[24]:


df = fdr.DataReader('005930', '2022')


# In[25]:


df = fdr.DataReader('005930', '2022')
df['Close'].plot();


# In[26]:


# 한국주식 (삼성전자)
df = fdr.DataReader('323410', '2022')
df['Close'].plot();


# In[28]:


df['Close'].plot();


# In[31]:


df['Change'].plot();


# In[ ]:




