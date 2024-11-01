10 <- a
a <- 10

total <- 5050    
total
print(total)
cat('합계 :', total)

#_____________________________________________________________________

# 변수를 이용한 산술연산
a <- 10          # 변수 a에 10을 저장
b <- 20          # 변수 b에 20을 저장
c <- a+b         # 변수 a, b에 저장된 값을 더하여 변수 c에 저장
print(a)
print(b)
print(c)

#하나의 변수에는 하나의 값만 저장가능
num <- 2, 5



abc <- 850      # 어떤 작업을 하려는 것인지 알기 어렵다.
mid.sum <-850   # 중간 합계를 850을 저장하려는 것임을 예상

a <- sqrt(120)  # 제곱근을 구하는 함수로서의 sqrt
a
sqrt <- 340     # 변수명으로서의 sqrt
sqrt

#숫자형과 문자형형
age.1 <- 20
age.2 <- 25
print(age.1 + age.2)
name.1 <- 'john'
print(name.1)
grade.1 <- '3'
print(age.1 + grade.1)


#논리형
5 > 3          # 비교연산
2 > 7          # 비교연산
TRUE + TRUE    # 산술연산에서는 TRUE는 1
a <- TRUE
b <- F

a
b
a+b


#특수한 값들들
addr <- NULL
print(addr)

a <- NA
b <- 'NA'
a
b

1/0
-2/0
sqrt(-5)



salt <- 50
water <- 100
result <- salt / (salt + water) *100
result <- round(result, 2)
cat("소금 =", salt, ", 물 =",water, " : 농도 =", result, "%")

salt <- 70
water <- 110
result <- salt / (salt + water) *100
result <- round(result, 2)
cat("소금 =", salt, ", 물 =",water, " : 농도 =", result, "%")

#___________________________________________________________________________
# 벡터의 개념 (코드)
socre.1 <- 68; socre.2 <- 95; socre.3 <- 83; socre.4 <- 76;
socre.5 <- 90;
socre.6 <- 80; socre.7 <- 85; socre.8 <- 91; socre.9 <- 82;
socre.10 <- 70;
total <- socre.1 + socre.2 +socre.3 +socre.4 +socre.5 +
            socre.6 + socre.7 +socre.8 +socre.9 +socre.10
avg <- total / 10        #10명의 평균 계산
avg                      #평균  출력


socre <- c(68,95,83,76,90,80,85,91,82,70)
mean(socre)        #평균 출력

#____________________________________________________________________________

x <- c(1,2,3)                # 숫자형 벡터
y <- c('a','b','c')          # 문자형 벡터
z <- c(TRUE,TRUE,FALSE,TRUE) # 논리형 벡터
w <- c(1,2,3, 'a','b','c')   # 숫자형,문자형 벡터
x
y
z
w

v1 <- 50:90          # 50~90까지 연속적으로 숫자를 실행
v1

v2 <- c(1,2,5, 50:90)    # 1 2 5 와 50~90까지 연속적 숫자 실행
v2

v3 <- seq(1,101,3)      # 시작, 종료, 간격
v3

v4 <- seq(0.1,1.0,0.1)  
v4

seq(0, 1, length.out = 11)
seq(stats::rnorm(20)) # effectively 'along'
seq(1, 9, by = 2)     # matches 'end'
seq(1, 9, by = pi)    # stays below 'end'
seq(1, 6, by = 3)
seq(1.575, 5.125, by = 0.05)
seq(17) # same as 1:17, or even better seq_len(17)

v5 <- rep(1,times=5)    # 1을 5번 반복
v5

v6 <- rep(1:5,times=3)   # 1,2,3,4,5를 3번 반복   , times <- 반복횟수  
v6

v7 <- rep(c(1,5,9), times=3) # 1,5,9를 3번 반복
v7

v8 <- rep(c('a','b','c'), each=3)  # a,b,c를 각각 3번 반복
v8

rep(1:4, 2)
rep(1:4, each = 2)       
rep(1:4, c(2,2,2,2))     
rep(1:4, c(2,1,2,1))
rep(1:4, each = 2, length.out = 4)    
rep(1:4, each = 2, length.out = 10)   
rep(1:4, each = 2, times = 3)

absent <- c(8,2,0,4,1)      # absent 벡터에 결근 인원수 저장
absent
names(absent)
names(absent) <- c('Mon','Tue', 'Wed','Thu','Fri')  #값들의 이름을 입력
absent
names(absent)

d <- c(1,4,3,7,8)
d               # 벡터 전체를 출력  
d[1]
d[2]
d[3]
d[4]
d[5]
d[6]

d <- c(1,4,3,7,8)
d[c(1,3,5)]         
d[1:3]              
d[seq(1,5,2)]       
d[-2]           # -는 '제외하고'의 의미       
d[-c(3:5)]

#_______________________________________________________________________________

# 이름으로 값을 추출하기
sales <- c(640,720,680,540)    # 1~4월 매출액
names(sales) <- c('M1','M2','M3','M4') # 매출액에 월을 이름으로 붙임
sales                   # 1~4월 매출액 출력
sales[1]                # 1월 매출액 출력
sales['M2']             # 2월 매출액 출력
sales[c('M1','M4')]     # 1월, 4월 매출액 출력

#벡터에 저장된 원소값 변경
v1 <- c(1,5,7,8,9)
v1
v1[2] <-3   # v1의 두번째 값을 3으로 변경
v1
v1[c(1,5)] <- c(10,20)
v1       
v1 <- c(100,200,300)
v1

# 적금 만기 금액 계산
customer <- c('kim','lee','park','choi','seo')
deposit <- c(5000000,4500000,4000000,5500000,6000000)
rate <- c(3.5,3,4,5,4.5)
period <- c(2,2,5,7,4)

# 원금, 이율, 기간 각 사람의 이름으로 설정 
names(deposit) <- customer
names(rate) <- customer
names(period) <- customer

# 변수를 만든다.
who <- customer

# 계산식
sum <- deposit[who] * (1 + rate[who] / 100)^ period[who]
sum

y <- sqrt(100)  # 100의 제곱근을 구하여 변수 y에 저장
y

d <- c(1,7,4,2,3)
sort(d)                          # 벡터 d의 값들을 오름차순으로 정렬
sort(d,decreasing = TRUE)        # 벡터 d의 값들을 내림차순으로 정렬


sort(x=d,decreasing = FALSE)     #정식 문법
sort(d,FALSE)                    #매개변수 이름의 생략

sort(x=d, FALSE)
sort(d,decreasing = FALSE)       #정식 문법
sort(x=d)                        #선택적 매개변수의 생략
sort(d)                          #매개변수명의 생략

as.Date("03-04-2024",format ='%d-%m-%Y')
as.Date("2024-04-03")

