# ds_625_tmp.py (6.25전쟁 전사자 데이터)

import os, re, usecsv

ds_625 = usecsv.opencsv('ds_625.csv')

total = 0 # 전사자 총합

for i in ds_625[1:]:
    print('기준일자:{}, 발굴년도:{}, 아군국군:{}'.format(i[0], i[1], i[2]))
    total += int(i[2])


print('\n아군 전사자 총합 : ', total)
