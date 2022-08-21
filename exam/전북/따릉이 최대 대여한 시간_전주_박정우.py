import os, re, csv
import usecsv


bicycle = usecsv.opencsv('bicycle_2022.csv')
bicycle_master = usecsv.opencsv('bicycle_master.csv')

hours = [0 for i in range(24)]

for use in bicycle[1:]:
    use[1]='0'*(4-len(use[1]))+use[1]
    hours[int(use[1][0:2])]+=1
        
mx=max(hours)
print(f'최대 대여횟수 : {mx}')      

mx_id=hours.index(mx)
print(f'최대 대여시간대 : {mx_id}')

print(hours)
