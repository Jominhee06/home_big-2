import sklearn.datasets  # 라이브러리 에서 제공 하는 데이터 셋 모듈
import matplotlib.pyplot as plt

digits=sklearn.datasets.load_digits() # 숫자 이미지 데이터를 로드

for i in range(50):
    plt.subplot(5, 10, i+1) # 3개는 순서 대로 1)행의 수, 2)열의 수, 3)번호를 나타 낸다.
    plt.axis("off") # N차원 배열을 정의할 때 사용 되기도 하며 여러 연산 과정 에서의 기준 으로도 쓰인다.
    plt.title(digits.target[i])
    plt.imshow(digits.images[i], cmap="Grays")

plt.show()