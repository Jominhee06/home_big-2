import pandas as pd
import matplotlib as plt

# CSV 파일을 활용하여, 데이터프레임으로 변환
df = pd.read_csv('D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD.csv', header=None)  # 옵션 사용
print(df.head())
print("\n")

df.columns = ['year','CD_rate','change']
df.set_index('year',inplace=True)
print(df.head)
df.to_csv("D:/HT_24050211003_조민희/pycharm_project_test/bok_statistics_CD_2.csv")
print('\n')

df.plot()
plt.pyplot.show()

df['CD_rate'].plot()
plt.pyplot.show()

df['change'].plot()
plt.pyplot.show()