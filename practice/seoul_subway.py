# seoul_subway.py

import glob
import pandas as pd

files = glob.glob('CARD*')
#print(files)

#f2 = files[0]
#pd.read_csv(f2, encoding='cp949').dtypes

df_list = []

for file in files:
    try:
        raw = pd.read_csv(file, encoding='cp949', parse_dates=[0])
        df_list.append(raw)
    except:
        raw = pd.read_csv(file, encoding='utf-8', parse_dates=[0])
        df_list.append(raw)

df = pd.concat(df_list)

df.reset_index(drop=True, inplace=True)

#print(df.info)
#print(df.isnull().sum(0))

df = df.drop('등록일자', axis=1)
df.insert(1, 'year', df['사용일자'].dt.year)
df.insert(2, 'month', df['사용일자'].dt.month)
df.insert(3, 'day', df['사용일자'].dt.day)

#print(df)
#print(df.dtypes)


df['total'] = df['승차총승객수'] + df['하차총승객수']

#print(df)

# 우선 전체적으로 total을 기준으로 내림차순해서 살펴보자
#print(df.sort_values(by='total', ascending=False).head(10)) # 잠실이 가장 많음

#승하차 승객수가 가장 많은 상위 10개역 추출
# 역명으로 groupby해서 합계를 구하고, total 기준으로 내림차순하여 출
#print(df.groupby('역명').sum().sort_values(by='total', ascending=False).head(10))

# 데이터프레임에서 인덱스만 추출해서 top10_stations에 저장
top10_stations = df.groupby('역명').sum().sort_values(by='total', ascending=False)[['total']].head(10).index
# print(top10_stations)

#isin 메서드를 사용하여 top10_stations만 뽑는 bool 시리즈 생성

top10_stations_cond = df['역명'].isin(top10_stations)
# print(top10_stations_cond)

top10 = df[top10_stations_cond]
# print(top10)

# top10에서 승객 수가 많은 5개의 노선만 추출
top10.노선명.unique()

# 11개의 노선에서 승객수의 합을 내림차순하여 확인
top10.groupby('노선명').sum().sort_values(by='total', ascending=False)

# head로 상위 5개만 추출
top10.groupby('노선명').sum().sort_values(by='total', ascending=False).head()

# top5 line을 뽑아내는 boolean series 생성
top5_line = top10.groupby('노선명').sum().sort_values(by='total', ascending=False).head().index

top5_line_cond = df['노선명'].isin(top5_line)
#print(top5_line_cond)

# 잘 만들어진 두개의 조건을 & 를 이용해 df를 걸러내보자
# top10_stations : 강남, 잠실(송파구청), 홍대입구, 고속터미널, 서울역, 신림, 선릉,
#사당, 구로디지털단지, 가산디지털단지
# top5_lines :  2호선, 7호선, 3호선, 1호선, 4호선

top = df[top10_stations_cond & top5_line_cond]

top.sort_values(by='total', ascending=False)

month_station = top.pivot_table(index='month', columns='역명', values='total')
print(month_station)






                        



