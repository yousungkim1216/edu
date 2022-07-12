# popSeoul.py

import os, re, usecsv

os.chdir(r'C:\doit\practice')
total = usecsv.opencsv('popSeoul.csv')

for i in total [:5]:
    print(i)

    
