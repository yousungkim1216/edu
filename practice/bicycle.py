# bicycle.py (따릉이)

import os, re, csv
import usecsv


bicycle = usecsv.opencsv('bicycle_2022.csv')
bicycle_master = usecsv.opencsv('bicycle_master.csv')

master = {}

#a['name'] = 'pey' 패턴 사용

for m in bicycle_master[1:]:
    code = m[0]
    address = m[1] + " " + m[2]
    master[code] = address

#print(meta)

for use in bicycle[1:]:
    if(use[2] != use[3]):
        print('시작대여:{}\n 종료대여:{}'.format(master.get(use[2]), master.get(use[3])))
    else:
        pass
        print('시작과 종료 모두 {} 보관소.'.format(master.get(use[2])))

       
# 시작/종료 대여소 빈도? pandas에서 활용가능
