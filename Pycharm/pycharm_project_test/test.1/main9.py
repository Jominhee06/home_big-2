import numpy as np
import matplotlib.pyplot as plt

# 텐서플로의 케라스 API에서 필요한 함수들을 불러옵니다.
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 데이터 준비
x = np.array([[2,0], [4,4], [6,2], [8,3]])# 2D 배열로 변환
y = np.array([81, 93, 91, 97])

# 모델 정의
model = Sequential()

# 입력 변수가 두 개(학습 시간, 과외 시간)이므로 input_dim에 2를 입력
model.add(Dense(1, input_dim=2, activation='linear'))

# 모델 컴파일
model.compile(optimizer='sgd', loss='mse')

model.fit(x, y, epochs=2000)

hour = 7
private_Class = 4
prediction = model.predict(np.array([[hour,private_Class]]))  # 2D 배열로 변환
print("%.f시간을 공부하고 %.f시간의 과외를 받을 경우, 예상 점수는 %.02f점입니다." % (hour,private_Class,prediction))