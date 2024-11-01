job.type <- 'A'
if (job.type == 'B') {
    bonus <- 200
} else {
    bonus <- 100
}
print(bonus)
#-------------
a <-10
if(a<5) {
    print(a)
} else {
    print(a*10)
    print(a/10)
}
#------------
a <- 10
b <- 20
if(a>5 & b>5){           # and
   print(a+b)
}
if (a>5 | b>30){         # or
    print(a*b)
}
#------------

job.type <- 'A'
bonus <- 100
if(job.type == 'B'){
   bonus <- 200
}
print(bonus)

#-------------

# ifelse를 이용한 처리
a <- 10
b <- 20

if(a>b){
   c <- a
} else {
   c <- b
}
print(c)

a <- 10
b <- 20

# ifelse를 이용한 처리
c <- ifelse(a>b, a, b)
print(c)

#------------

score <- 85

if (score > 90){
    grade <- 'A'
} else if(score > 80){
    grade <- 'B'
} else if(score > 70){
    grade <- 'C'
} else if(score > 60){
    grade <- 'D'
} else{
    grade <- 'F'
}
print(grade)

#------------

# 회원 등급 분류하고 혜택 부여하기

library(svDialogs)
purchase <- dlgInput('Enter the purchase amount') $res
purchase <- as.numeric(purchase)

type <- NULL
ratio <- NULL

if (purchase >= 300000){
    type <- '플래티넘'
    ratio <- 0.07
} else if(purchase >= 200000){
    type <- '골드'
    ratio <- 0.05
} else if(purchase >= 100000) {
    type <- '실버'
    ratio <- 0.03
} else {
    type <- '프렌즈'
    ratio <- 0.01
}

cat('고객님은', type, '회원으로 구매액의', ratio*100, '%가 적립됩니다.')

#------------

# for문

for(i in 1:5){
  print('*')
  print(i)
}

for(i in 6:10){
  print('*')
  print(i)
}

# R구구단
for(i in 1:9){
  print(i)
  cat('2 *', i,'=',2*i, '\n')
  print('2 *', i,'=',2*i, '\n')
}

#-------------

# 짝수
for(i in 1:20){
  if(i%%2==0){
    cat(i, ' ')
  }
}

# 홀수
for(i in 1:20){
  if(i%%2!=0){
    cat(i,' ')
  }
}

#-------------

sum <- 0
for(i in 1:100){
    sum <- sum+i
}
print(sum)

#-------------

# 꽃잎의 길이에 따라 데이터
norow <- nrow(iris)          # iris의 행의 수
mylabel <- c()
for(i in 1:norow){
  if(iris$Petal.Length[i] <= 1.6){     # 꽃잎의 길이에 따라 레이블 결정
      mylabel[i] <- 'L'
  } else if(iris$Petal.Length[i] >= 5.1){
      mylabel[i] <- 'H'
  } else {
      mylabel[i] <- 'M'
  }
}
print(mylabel)
newds <- data.frame(iris$Petal.Length, mylabel)  # 꽃잎 길이와 레이블 결합
head(newds)

#-------------

#while문
sum <- 0
i <- 1
while(i <=100){
  sum <- sum+i
  i <- i+1
}
print(sum)

#-------------

# apply() 계열 함수
apply(iris[,1:4], 1, mean) # 행 방향으로 함수 적용  
apply(iris[,1:4], 2, mean) # 열 방향으로 함수 적용

#-------------

# 자격증 합격 여부 판단하기
sub1 <- c(14,16,12,20,8,6,12,18,16,10)
sub2 <- c(18,14,14,16,10,12,10,20,14,14)
sub3 <- c(44,38,30,48,42,50,36,52,54,32)
score <- data.frame(sub1, sub2, sub3)

total <- apply(score, 1, sum)
scoreset <- cbind(score, total)
head(scoreset)

result <- c()

for(i in 1:nrow(scoreset)){
  if(scoreset[i,1] < 20*0.4 | scoreset[i,2] < 20*0.4 |
     scoreset[i,3] < 60*0.4){
      result[i] <- '불합격'
  }else if(scoreset[i,4] >= 60){
      result[i] <- '합격'
  }else{
      result[i] <- '불합격'
  }
  cat(i, '번째 응시생은', result[i], '입니다. \n')
}

#--------------