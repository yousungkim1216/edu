#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

res = requests.get(url)
# html 정보에서 text정보만 추출
html = res.text
soup = BeautifulSoup(html, 'html.parser')

# my_stock 변수에 select 할 내용을 찾아서 넣어준다
my_stock = soup.select('.lst_pop')

for stock_name in my_stock:
    print(stock_name.text)


# In[2]:


import urllib.request

page = urllib.request.urlopen(url)

html = page.read().decode('cp949')
soup = BeautifulSoup(html, 'html.parser')

soup.select('span.num')

# 우리가 찾는 값
soup.select('span.num')[1]
# string 속성만 추출
soup.select('span.num')[1].string
# float 자료형 변환
float(soup.select('span.num')[1].string.replace(',', ''))


# In[3]:


# input으로 id = 'KOSPI_now' 처럼 지정
soup.find(id = 'KOSPI_now')
# string 속성을 가져와 원하는 데이터까지 도달
soup.find(id = 'KOSPI_now').string


# In[4]:


# 코스피 등락률 크롤링
soup.find(id = 'KOSPI_change')

soup.find(id = 'KOSPI_change').contents

soup.find(id = 'KOSPI_change').contents[2]

soup.find(id = 'KOSPI_change').contents[2].split()

soup.find(id = 'KOSPI_change').contents[3].string


# In[5]:


def NS_users_crawler(codes, page):
    # User-Agent 설정
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    result_df = pd.DataFrame([])

    n_ = 0
    for page in range(1, page):
        n_ += 1
        if (n_ % 10 == 0):
            print('================== Page ' + str(page) + ' is done ==================')
        url = "https://finance.naver.com/item/board.naver?code=%s&page=%s" % (codes, str(page))
        # html → parsing
        html = requests.get(url, headers=headers).content
        # 한글 깨짐 방지 decode
        soup = BeautifulSoup(html.decode('euc-kr', 'replace'), 'html.parser')
        table = soup.find('table', {'class': 'type2'})
        tb = table.select('tbody > tr')

        for i in range(2, len(tb)):
            if len(tb[i].select('td > span')) > 0:
                date = tb[i].select('td > span')[0].text
                title = tb[i].select('td.title > a')[0]['title']
                views = tb[i].select('td > span')[1].text
                pos = tb[i].select('td > strong')[0].text
                neg = tb[i].select('td > strong')[1].text
                table = pd.DataFrame({'날짜': [date], '제목': [title], '조회': [views], '공감': [pos], '비공감': [neg]})
                result_df = result_df.append(table)

    return result_df


# In[6]:


data = NS_users_crawler("035720", 3)
data.head(10)


# In[7]:


code = '005930'
URL = f"https://finance.naver.com/item/main.nhn?code={code}"
r = requests.get(URL)
df = pd.read_html(r.text)[3]
df


# In[8]:


# 최근연간실적, 최근분기실적 분할
df.columns

# 첫번째 컬럼을 인덱스로 설정
#('주요재무정보','주요재무정보',주요재무정보') 를 '주요재무정보' 로 변경
df.set_index(df.columns[0],inplace=True)
df.index.rename('주요재무정보', inplace=True)

#'IFRS연결' 을 버려야 하니 droplevel을 씁니다. 지금 컬럼은 (0,1,2) 형식의 튜플로 되어있으니 
# 2번째를 droplevel을 하면 됩니다.
df.columns = df.columns.droplevel(2)
df.columns


# In[9]:


annual_date = pd.DataFrame(df).xs('최근 연간 실적',axis=1)
quater_date = pd.DataFrame(df).xs('최근 분기 실적',axis=1)

annual_date
quater_date


# In[10]:


import FinanceDataReader as fdr

df_krx = fdr.StockListing('KRX')

# 개별 종목 가격 데이터 가져오기
#df = fdr.DataReader('종목코드', '시작일자'. '종료일자')

# 한국주식 (삼성전자)
#df = fdr.DataReader('005930', '2021', '2022')
#df
# 미국주식 (APPLE) # df['Close'].plot();
#df = fdr.DataReader('AAPL', '2022')
#df['Close'].plot();


# ETF 데이터 가져오기 # 미국(ETF/US), 일본(ETF/JP)
#df_etf = fdr.StockListing('ETF/KR')
#df_etf

# KODEX 200선물인버스2X 사례
df_inver = fdr.DataReader('252670')
df_inver


# In[11]:


pip install -U finance-datareader

