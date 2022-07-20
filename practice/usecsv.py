# usecsv.py

import csv, re, os

def opencsv(filename): # 리스트로 반환
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

def writecsv(filename, the_list): # 파일 Write
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)
        
def switch(listName): # Float 자료형으로 변환
    for i in listName:        
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
    return listName
