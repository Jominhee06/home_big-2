import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2,4,6,8])
x2 = np.array([0,4,2,3])
y = np.array([81,93,91,97])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1,x2,y);
plt.show()

a1 = 0
a2 = 0
b = 0

lr = 0.01

epochs = 2001

n = len(x1)

for i in range(epochs):

  y_pred = a1*x1+a2*x2+b
  error = y - y_pred

  a1_diff = (2/n) * sum(-x1 * (error))
  a2_diff = (2/n) * sum(-x2 * (error))
  b_diff = (2/n) * sum(-(error))

  a1 = a1 - lr *a1_diff
  a2 = a2 - lr * a2_diff
  b = b -lr * b_diff

  if i % 100 == 0:
    print("epoch = %.f, 기울기=%.04f,기울기2=%.04f,절편=%.04f" %(1,a1,a2,b))

print("실제 점수 : ", y)
print("예측 점수 : ", y_pred)