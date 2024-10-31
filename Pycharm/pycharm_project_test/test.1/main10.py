import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2,4,6,8,10,12,14])
y = np.array([0,0,0,1,1,1,1])

model = Sequential()
model.add(Dense(1,input_dim=1,activation='sigmoid'))

model.compile(optimizer='sgd',loss='binary_crossentropy')
model.fit(x,y,epochs=5000)

plt.scatter(x,y)
plt.plot(x, model.predict(x),'r')
plt.show()

hour = np.array([7])
prediction = model.predict([hour])
print("%.f시간을 공부할 경우, 합격 예상 확률은 %.01f%%입니다." %(hour,prediction * 100))