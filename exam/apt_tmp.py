# apt_tmp.py ==> 202207 2010년 이후 건축된 84평 이상 7억 미만 대구 아파트 매매 데이터

import os, re, usecsv

os.chdir(r'c:\doit\practice')

apt_tmp = usecsv.opencsv('apt_202207.csv') # 202207 전국 아파트 매매거래 데이터
apt = usecsv.switch(apt_tmp)

new_list = [['지역', '아파트명', '전용면적', '거래금액', '층', '건축년도']] 

for i in apt:
    try:
        if i[5] > 84 and i[8] <= 70000 and re.search('대구', i[0]) and i[-5] > 2010:
            new_list.append([i[0], i[4], i[5], i[8], int(i[-6]), int(i[-5])])
    except:
        pass
    

usecsv.writecsv('over84_lower70000_daegu.csv', new_list)
