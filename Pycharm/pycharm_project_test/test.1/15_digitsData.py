from string import digits

import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("데이터의개수=", len(digits.images))
print("이미지데이터=", digits.images[0])
print("무슨숫자인가=", digits.images[0])