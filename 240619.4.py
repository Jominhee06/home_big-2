import matplotlib.pyplot as plt
from pandas.plotting import table
import pandas as pd
import os

#################################
## 데이터프레임 생성
#################################
# 실제 파일 경로로 변경합니다.
csv_file_path = 'D:/Joo.min.hee/IOT강의/Source.1/res/data.csv' # 실제 CSV 파일 경로를 입력합니다.
df = pd.read_csv(csv_file_path)

#################################
## 결과 저장 폴더 생성
#################################
os.makedirs("res/stock_report", exist_ok=True)

#################################
## 차트 그리기
#################################
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['close'])
plt.xlabel('date')
plt.ylabel('close')

#################################
## 차트 저장 및 출력하기
#################################
company = '삼성전자' # 회사 이름을 설정합니다.
chart_fname = os.path.join("res/stock_report", f'{company}_chart.png')
plt.savefig(chart_fname)
plt.show()

#################################
## 일별 시세 그리기
#################################
plt.figure(figsize=(15,4))
ax = plt.subplot(111, frame_on=False) # 눈에 보이지 않는 프레임
ax.xaxis.set_visible(False) # x축 숨기기
ax.yaxis.set_visible(False) # y축 숨기기
df = df.sort_values(by=['date'], ascending=False)
table(ax, df.head(10), loc='center', cellLoc='center', rowLoc='center') # df는 데이터 프레임

#################################
## 일별 시세 저장하기
#################################
table_fname = os.path.join("res/stock_report", f'{company}_table.png')
plt.savefig(table_fname)


