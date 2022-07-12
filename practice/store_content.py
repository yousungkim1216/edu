# store_content.py

import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'c:\doit\practice')

article1 = 'https://v.daum.net/v/20220712080023052'
soup = bs(ur.urlopen(article1).read(), 'html.parser')

f = open('article1.txt', 'w', encoding='utf-8')

for i in soup.find_all('p'):
    f.write(i.text)


f.close()

