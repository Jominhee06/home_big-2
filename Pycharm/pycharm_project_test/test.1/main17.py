# 데이터프레임 요약정보 확인
import pandas as pd

# csv 파일을 활용하여 데이터프레임으로 변환
df = pd.read_csv('D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD.csv', header=None)  # 옵션 사용

print(df.head())
print('\n')
print(df.info())