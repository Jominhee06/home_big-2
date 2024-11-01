# 데이터셋의 기본 정보
dim(iris)
nrow(iris)
ncol(iris)
colnames(iris)
head(iris)      #데이터셋의 앞부분 일부 보기
tail(iris)      #데이터셋의 뒷부분 일부 보기

str(iris)
iris[,5]
levels(iris[,5])           # 품종의 종류 보기(중복 제거)
table(iris[,"Species"])    # 품종의 종류별 행의 개수 세기

# 행별 열별로 합계와 평균 계산하기
colSums(iris[,-5])     # 열별 합계
colMeans(iris[,-5])    # 열별 평균
rowSums(iris[,-5])     
rowMeans(iris[,-5])

# 행과 열의 방향 변환하기
z <- matrix(1:20, nrow=4, ncol=5)
z
t(z)       

#_______________________________________________________________________________

# 조건에 맞는 행과 열의 값 추출하기
IR.1 <- subset(iris, Species=='virginica')
IR.1
IR.2 <- subset(iris, Sepal.Length>5.0 & Sepal.Width>4.0)

IR.2
IR.2[,c(2,4)]

# 관련 코드
subset(iris, Species=='virginica')
subset(iris,Species==levels(iris[,5])[3])

# 산술연산 적용
a <- matrix(1:20,4,5)
b <- matrix(21:40,4,5)
a
b

2*a

a+b

a <- a*3
b <- b-5
a
b

# 자료구조 확인하기
class(iris)
class(state.x77)
is.matrix(iris)
is.data.frame(iris)
is.matrix(state.x77)
is.data.frame(state.x77)

# 매트릭스를 데이터프레임으로 변환
is.matrix(state.x77)
st <- data.frame(state.x77)
head(st)
class(st)

# 데이터프레임을 매트릭스로 변환
is.data.frame(iris[,1:4])
iris.m <- as.matrix(iris[,1:4])
head(iris.m)
class(iris.m)

# 데이터프레임만 적용되는 열 추출 방법
iris[,"Species"]
iris[,5]
iris["Species"]
iris[5]
iris$Species
#_______________________________________________________________________________

# 예제문제(벚나무 판매하기)
class(trees)
str(trees)

girth.mean <- mean(trees$Girth)

candidate <- subset(trees, Girth >= girth.mean & Height > 80 &
                      Volume > 50)

candidate
nrow(candidate)

# 종업원의 팁 계산하기
install.packages('reshape2')
library(reshape2)
str(tips)

is.matrix(tips)
class(tips)
head(tips)

table(tips$smoker)

table(tips$time)

table(tips$day)

dim(dinner <- subset(tips, time == 'Dinner'))
dim(lunch <- subset(tips, time=='Lunch'))

table(dinner$day)
table(lunch$day)

colMeans(dinner[c('total_bill','tip','size')])
colMeans(lunch[c('total_bill','tip','size')])

tip.rate <- tips$tip/tips$total_bill
mean(tip.rate)

dinner.rate <- dinner$tip/dinner$total_bill
mean(dinner.rate)

lunch.rate <- lunch$tip/lunch$total_bill
mean(lunch.rate)

round(mean(tip.rate),2)



