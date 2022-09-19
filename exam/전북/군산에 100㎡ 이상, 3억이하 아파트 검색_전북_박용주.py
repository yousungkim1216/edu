>>> import os, re
>>> os.chdir(r'c:\doit\practice')
>>> import usecsv
>>> apt = usecsv.switch(usecsv.opencsv('apt_202208.csv'))
>>> apt[:3]

>>> len(apt)

>>> apt[0]

>>> for i in apt[:6]:
...     print(i[0])

#거래금액은 오른쪽에서 7번째 원소 i[-7]
>>> for i in apt[:6]:
...     print(i[0],i[4],i[-7])

#군산에 100㎡ 이상, 3억이하 아파트 검색

>>> new_list = []
>>> for i in apt:
...     try:
...         if i[5]>=100 and i[-7] <= 30000 and re.match('전라북도 군산시',i[0]):

#시군구, 아파트 단지명, 가격을 new_list에 저장
...             new_list.append([i[0], i[4], i[-7]])
...     except: pass

#writecsv()함수로 new_list 객체에 저장된 csv형 리스트를 csv형 리스트를 csv파일로 저장함
>>> usecsv.writecsv('over100_lower30000.csv',new_list)
#over120_lower30000이라는 엑셀 파일에 
#전라북도 군산시 나운동에 있는 3개 아파트( 동신맨션1차 7300, 현대아파트 25700, 현대아파트(2차) 19000 )
#전라북도 군산시 미룡동에 있는 금광베네스타 29300 
#총 4개의 데이터가 저장되어 있다.