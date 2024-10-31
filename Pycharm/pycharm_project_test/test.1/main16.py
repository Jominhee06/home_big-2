# 데이터 내용 확인하기
import pandas as pd

# csv 파일을 활용하여, 데이터 프레임으로 변환
df = pd.read_csv('D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD.csv')

print(df.head())
print('\n')
print(df.head(3))
print('\n')
print(df.tail())
print('\n')
print(df.tail(3))