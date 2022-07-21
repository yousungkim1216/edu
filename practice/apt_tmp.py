# apt_tmp.py

import os, re, usecsv

apt_tmp = usecsv.opencsv('apt_202207.csv')
apt = usecsv.switch(apt_tmp)

new_list = [['지역', '아파트명', '전용면적', '거래금액']]

for i in apt:
    try:
        if i[5] > 84 and i[8] >= 100000 and re.search('제주', i[0]):
            #print(i[0], i[4], i[5], i[8])
            new_list.append([i[0], i[4], i[5], i[8]])
    except:
        pass

usecsv.writecsv('over84_lower100000.csv', new_list)

    
