import os, re, usecsv

os.getcwd() # 현재 작업 디렉토리를 보여줌
os.listdir() # 파일목록을 리스트 형태로 반환함

filelist=[] # 'apt_000000.csv' 패턴의 파일만 리스트에 담는다.
for filename in os.listdir():
    if re.match(r'apt_\d{6}.csv',filename):
        filelist.append(filename)
##print(filelist)

apt_total=[] # filelist에 있는 모든파일을 하나(리스트)로 모은다.
start=0
for apt in filelist:
    apt_total+=usecsv.opencsv(apt)[start:]
    start=1
##print(len(apt_total))
    
apt_total=usecsv.switch(apt_total)
# 하나로 모은 데이터에서 숫자에 ','가 있으면 제거하고 float형으로 변환한다.

fn=apt_total[0]

n=lambda x:fn.index(x)
fn[0]='지역'
fn[4]='아파트명'
fn[5]='전용면적'
fn[8]='거래금액'

local=input("알고싶은 지역을 space로 구분하여 입력 : ").split()

def local_class(city):
    local_dict={}

    new_list = [['월','지역', '아파트명', '전용면적', '거래금액']]

    for i in apt_total[1:]:   
        try:
            if i[n('전용면적')] >= 80 and re.search(city, i[n('지역')]):
                local_city=re.search(city, i[n('지역')]).group()
                new_list.append([int(i[n('계약년월')])%100,local_city,
                                 i[n('아파트명')],i[n('전용면적')], i[n('거래금액')]])
                key=local_city+str(int(i[n('계약년월')]))[4:]  # 전주06
                if local_dict.get(key)!=None :
                    local_dict[key][0]+=1
                    if local_dict[key][1]<i[n('거래금액')] :
                        local_dict[key][1]=i[n('거래금액')]
                else:
                    local_dict[key]=[1,i[n('거래금액')]]
        except :
            pass
    return local_dict

print(f'{"지역":4} {"월":>2} {"거래건수":>4} {"최대금액":>8}')
print('='*32)

for city in local:
    local_dict=local_class(city)
    for key,value in local_dict.items():
        print(f'{key[:-2]:<4} {key[-2:]:>2} {value[0]:>8} {int(value[1]):>12}')
    print('='*32)
##        
##<결과>
##알고싶은 지역을 space로 구분하여 입력 : 전주 군산 익산 의정부
##지역    월 거래건수     최대금액
##================================
##전주   06      252        92000
##전주   07      197        85300
##전주   08       45        76000
##================================
##군산   06      118        51500
##군산   07       64        58000
##군산   08       16        35000
##================================
##익산   06       73        52500
##익산   07       57        44000
##익산   08       20        31000
##================================
##의정부  06       50        69000
##의정부  07       39        65000
##의정부  08        6        58000
##================================





