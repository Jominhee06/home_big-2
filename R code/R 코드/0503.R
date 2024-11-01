z <- matrix(1:20, nrow=4, ncol=5)
z

z[2,3]     # 2행 3열에 있는 값
z[1,4]     # 1행 4열에 있는 값
z[2,]      # 2행에 있는 모든 값
z[,4]      # 4열에 있는 모든 값

z[2,1:3]          # 2행의 값 중 1~3열에 있는 값
z[1,c(1,2,4)] 
z[1:2,]
z[,c(1,4)]

z2 <- matrix(1:20, nrow=4, ncol=5, byrow=T)
z2

x <- 1:4
y <- 5:8
z <- matrix(1:20, nrow=4, ncol=5)

m1 <- cbind(x,y)
m1
m2 <- rbind(x,y)
m2
m3 <- rbind(m2,x)
m3
m4 <- cbind(z,x)
m4

#_______________________________________________________________________________

# 행과 열에 이름붙이기
score <- matrix(c(90,85,69,78,85,96,49,95,90,80,70,60), nrow=4)
score
rownames(score) <- c('John','Tom','Mark','Jane')
colnames(score) <- c('English','Math','Science')
score

score['John','Math']
score['Tom',c('Math','Science')]
score['Mark',]
score[,'English']
rownames(score)
colnames(score)
colnames(score)[2]     #score의 열의 이름 중 두 번째 값

m <- matrix(1:10 ,nrow=2)
m

#_______________________________________________________________________________

#햄버거 영양 성분 정보 제공하기
burger <- matrix(c(514,917,11,533,853,13,566,888,10),nrow = 3,byrow = T)
burger
rownames(burger) <- c('M','L','B')
colnames(burger) <- c('kcal','na','fat')
burger

burger['M','na']
burger['M',]
burger[, 'kcal'][3]

#햄버거 영양 성분 정보 추가하기
kcal <- c(514,533,566)
na <- c(917,853,888)
fat <- c(11,13,10)
menu <- c('새우','불고기','치킨')

burger <- data.frame(kcal, na, fat, menu)
burger

colnames(burger)
rownames(burger) <- c('M', 'L', 'B')

burger['M','na']
burger['M',]
burger[, 'kcal']
burger[c('M','B'), 'menu']
new <- burger['L',]

#바인드 추가!
burger2 <- rbind(burger,new)

#_______________________________________________________________________________

#데이터프레임 만들기 -> 2개 이상의 자료형으로 구조된 2차원자료구조
city <- c("Seoul","Tokyo","Washington")
rank <- c(1,3,2)
city.info <- data.frame(city,rank)
city.info

dim(burger)
nrow(burger)
ncol(burger)
colnames(burger)
head(burger)      # 데이터셋의 앞부분 일부 보기
tail(burger)

#_______________________________________________________________________________

#iris 데이터
iris[,c(1:2)]
iris[,c(1,3,5)]
iris[,c("Sepal.Length","Species")]
iris[1:5,]
iris[1:5,c(1,3)]
iris[c(1:4)]
iris[-5]

dim(iris)
nrow(iris)
ncol(iris)
colnames(iris)
head(iris)      # 데이터셋의 앞부분 일부 보기
tail(iris)

s <- colnames(iris)[5]
iris[,colnames(iris)[5]]

head(iris, 3) 

tail(iris, 4)

str(burger)              # 데이터셋 요약 정보 보기
iris[,5]                 # 품종 데이터 보기
levels(iris[,5][4])         # 품종의 종류 보기(중복 제거)
table(iris[,"Species"])  # 품종의 종류별 행의 개수 제거

iris$Sepal.Length # $ = 어떤 변수를 작동할지 선택가능!

str(integer)
as.integer(iris$Species)

#행별, 열별로 합계와 평균 계산하기
colSums(iris[,-5])            # 열별 합계
colMeans(iris[,-5])
rowSums(iris[,-5])
rowMeans(iris[,-5])           # 행별 평균
#_______________________________________________________________________________





