# issue_2022.py (폭염데이터)
# data.kma.go.kr

import os, re, csv

os.chdir(r'c:\doit\practice')
import usecsv


#issue = opencsv('issue_2022.csv')
issue = usecsv.switch(usecsv.opencsv('issue_2022.csv'))

for i in issue:
    try:
        if re.match('서울', i[1]) and i[3] > 32 and i[2] == 'O':
            print('일자:{}, 지점:{}, 최고체감온도:{}'.format(i[0], i[1], i[3]))
    except:
        pass
