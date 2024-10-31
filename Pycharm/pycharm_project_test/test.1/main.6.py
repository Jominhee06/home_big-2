import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 데이터 준비
x = np.array([2, 4, 6, 8])# 2D 배열로 변환
y = np.array([81, 93, 91, 97])

# 모델 정의
model = Sequential()

model.add(Dense(1, input_dim=1, activation='linear'))

# 모델 컴파일
model.compile(optimizer='sgd', loss='mse')

# 모델 훈련
model.fit(x, y, epochs=2000)

# 결과 시각화
plt.scatter(x, y)
plt.plot(x, model.predict(x), 'r')
#plt.legend()
plt.show()

# 예측
hour = np.array([7])
prediction = model.predict(([hour]))  # 2D 배열로 변환
print("%.f시간을 공부할 경우의 예상 점수는 %.02f점입니다." % (7, prediction))