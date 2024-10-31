import pandas as pd
import matplotlib as plt

# CSV 파일을 활용하여, 데이터프레임으로 변환
df = pd.read_csv('D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD_2.csv', header=0 , index_col=0)  # 옵션 사용
print(df.head())
print("\n")

# 히스토그램
df['CD_rate'].plot(kind='hist')
plt.pyplot.show()

df['change'].plot(kind='hist')
plt.pyplot.show()