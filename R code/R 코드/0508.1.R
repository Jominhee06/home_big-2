# 데이터셋 가져오기
age <- c(28,17,35,46,23,67,30,50)
age

# 정보 추출
young <- min(age)
old <- max(age)

#처리 결과 출력
cat('가장 젋은 사람의 나이는', young, '이고,',
    '가장 나이든 사람의 나이는',old,'입니다.\n')

getwd()  # 위치

#_______________________________________________________________________________

#화면에서 데이터 입력받기
install.packages('svDialogs')
library(svDialogs)
user.input <- dlgInput('연봉을 입력하세요')$res
user.input
income <- as.numeric(user.input)   # 문자열을 숫자로
income
tax <- income * 0.05               # 세금 계산
cat('세금: ', tax )

#print()함수와 cat()함수
x <- 26
y <-'입니다'
z <-c(10,20,30,40)
print(x)
print(y)
print(z)
print(iris[1:5,])
print(x,y) # 강제형변환에 의해 생성된 NA 입니다.

x <- 26
y <- '입니다'
z <- c(10,20,30,40)
cat(x,'\n')
cat(y,'\n')
cat(z,'\n')
cat(x,y,'\n')
cat(iris[1:5],'\n')
# 타입 'list'인 인자 1는 'cat'에 의하여 다루어 질 수 없습니다

#_______________________________________________________________________________

# 체질량 지수 계산하기ㅣ
library(svDialogs)

height <- dlgInput('Input height(cm)')$res
weight <- dlgInput('Input weight(kg)')$res

height <- as.numeric(height)
weight <- as.numeric(weight)

height <- height /100
bmi <- weight/(height^2)

cat('입력한 키는 ', height*100, 'cm, 몸무게는 ', weight, 'kg 입니다. \n' 
    ,sep="")

cat('BMI는 ', bmi, '입니다.', sep="")

getwd()
setwd('D:\\Rworks')
getwd()

setwd('D:/Rworks')
air <- read.csv('Rdata/airquality.csv', header = T)
head(air)
class(air)

str(air)

setwd('D:/Rworks')
my.iris <- subset(iris, Species=='setosa')
write.csv(my.iris, 'my_iris.csv',row.names = F)
my.iris <- subset(iris, Species=='setosa')
write.csv(my.iris, 'my_iris.csv',row.names = T)



