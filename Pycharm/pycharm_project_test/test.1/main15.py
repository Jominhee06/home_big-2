# pip install openpyxl
import pandas as pd

csv_file = 'D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD.csv'
# read_csv() 함수로 데이터프레임 변환
df1 = pd.read_csv(csv_file)
print(df1)
print('\n')

df1 = pd.read_csv(csv_file, header=None)  # 옵션 사용
print(df1)
print('\n')

df1 = pd.read_csv(csv_file, index_col=0) # 옵션 사용
print(df1)
print('\n')

df1 = pd.read_csv(csv_file, index_col=0,header=None) # 옵션 사용
print(df1)
print('\n')

# excal 파일 불러오기
excel_file = 'D:/HT_24050211003_조민희/pycharm_project_test/report_Key100Stat.xls'
# read_excal() 함수로 데이터 프레임 변환
df5 = pd.read_excel(excel_file,engine="openpyxl")
print(df5)
