# article_total.py

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'c:\doit\practice')

url = 'https://news.daum.net/';
soup = bs(ur.urlopen(url).read(), 'html.parser')

f = open('article_total.txt', 'w')

for i in soup.find_all('div', {"class":"item_issue"}):
    try:
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')

        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()

