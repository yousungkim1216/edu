# portal_cwr.py

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'c:\doit\practice')


news = 'https://news.daum.net/'
soup = bs(ur.urlopen(news).read(), 'html.parser')


headline = soup.find_all('div', {"class":"item_issue"})

for i in headline:
    print(i.text, '\n')
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    for j in soup3.find_all('p'):
            j.text

               
