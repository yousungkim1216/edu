# bicycle_tmp.py (따릉이)
# URL : https://www.data.go.kr/data/15099364/fileData.do

import os, re, usecsv

bicycle = usecsv.opencsv('bicycle_2022.csv')
bicycle_master = usecsv.opencsv('bicycle_master.csv')

code = dict()
for i in bicycle_master[1:]:
    code[i[0]] = i[1] + " " + i[2]

#for use in bicycle[:100]:
#    if(use[2] != use[3]):
#        print('시작대여:{}\n 종료대여:{}'.format(code.get(use[2]), code.get(use[3])))
#    else:
#        print('시작과 종료 모두 {} 대여소.'.format(code.get(use[2])))
