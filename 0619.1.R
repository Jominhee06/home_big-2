#원형 그래프
favorite <- c('WINTER','SUMMER','SPRING','SUMMER','SUMMER','FALL','FALL',
              'SUMMER','SPRING','SPRING')
favorite
table(favorite)  #도수분포 계산

# table(iris$Species)
ds <- table(favorite)
ds
pie(ds,main='선호 계절',   # 원그래프 작성
    radius = 1)

pie(ds,main='선호 계절',
    col=c('brown','red','green','black'),
    radius = 1)
#_______________________________________________________________________________

# 3D 원형 그래프
install.packages('plotrix')

library(plotrix)
pie3D(ds,main='선호 계절',
      labels = names(ds),
      labelcex = 1.0,        # 레이블의 폰트 크기
      explode = 0.1,
      radius = 1.5,
      col=c('brown','red','green','black'))

pie3D(ds,main='선호 계절',
      labels = names(ds),
      labelcex = 1.0,        # 레이블의 폰트 크기
      explode = 0.2,
      radius = 1.7,
      col=c('brown','pink','plum','palegreen'))

#_______________________________________________________________________________

# 선그래프
par(mfrow = c(2,2))
month = 1:12
late1 = c(5,8,7,9,4,6,12,13,8,6,6,4)
late2 = c(4,6,5,8,7,8,10,11,6,5,7,3)
plot(month,
     late1,
     main='지각생 통계',
     type='o',           # 그래프의 종류 선택(알파벳)
     lty=1,              # 선의 종류(line type) 선택
     lwd=1,              # 선의 굵기 선택
     xlab='Month',
     ylab='Late cnt'
)
lines(month,
      late2,
      type='b',
      col = 'blue')
#_______________________________________________________________________________

# 상자그림
dist <-cars[,2]
boxplot(dist, main='자동차 제동거리')

# 그룹이 있는 데이터의 상자그림(꽃잎의 길이)
boxplot(Petal.Length~Species,
        data=iris,                          # 데이터가 저장된 자료구조
        main='품종별 꽃잎의 길이',
        col=c('palegreen','brown','yellow'))

boxplot(iris$Petal.Length~iris$Species,
        main='품종별 꽃잎의 길이',
        col=c('palegreen','brown','yellow'))

# 자동차 데이터 분석
par(mfrow = c(2,2))

boxplot(mtcars$mpg)

boxplot(mtcars$mpg~mtcars$gear)

boxplot(mtcars$mpg~mtcars$vs)

boxplot(mtcars$mpg~mtcars$am)

grp <- rep('high', nrow(mtcars))
grp[mtcars$wt < mean(mtcars$wt)] <- 'low'
boxplot(mtcars$hp~grp)
#_______________________________________________________________________________

# 산점도
wt <- mtcars$wt        # 중량 데이터
mpg <- mtcars$mpg      # 연비 데이터
plot(wt,mpg,           # 2개 변수(x축,y축)
     main= '중량-연비 그래프',  # 제목
     xlab = '중량',             # x축 레이블
     ylab = '연비(MPG)',        # y축 레이블
     col = 'red',               # point의 color
     pch= 12)                   # point의 종류

plot(mpg~wt,data=mtcars,
     main= '중량-연비 그래프',  # 제목
     xlab = '중량',             # x축 레이블
     ylab = '연비(MPG)',        # y축 레이블
     col = 'red',               # point의 color
     pch= 15)                   # point의 종류

# 여러 변수들 간의 산점도
vars <- c('mpg','disp','drat','wt')
target <- mtcars[,vars]
head(target)
plot(target,
     main = 'Multi plots')

str(target)

# 그룹 정보가 있는 2개 변수의 산점도
iris.2 <- iris[,3:4]
levels(iris$Species)
group<-as.numeric(iris$Species)
group
color <- c('red','palegreen','blue')
plot(iris.2,
     main='Iris plot',
     pch=c(group),
     col=color[group])

legend(x='bottomright',                     # 범례의 위치
       legend =levels(iris$Species),        # 범례의 내용
       col=c('darkred','palegreen','blue'), # 색 지정
       pch=c(1:3))                          # 점의 모양

#_______________________________________________________________________________

# 자동차의 선팅 분석하기
install.packages(DAAG)
library(DAAG)
str(tinting)

plot(tinting$it,tinting$csoa)

# 선팅의 정도
group <- as.numeric(tinting$tint)           
color <- c('plum','green','darkblue')      # 점의 컬러
plot(tinting$it,tinting$csoa,
     pch=c(group),
     col=color[group])

# 연령대에 따라 언급한 두 가지 인식 시간
group <- as.numeric(tinting$tint)
color <- c('plum','palegreen')             # 점의 컬러
plot(tinting$it,tinting$csoa,
     pch=c(group),
     col=color[group])

library(DAAG)
str(socsupport)
help(socsupport)

# 조사 대상자의 연령별 비율을 3차원 원그래프
library(plotrix)
ds<-table(socsupport$age)
pie3D(ds, main= '연령 분포',
      labels = names(ds),
      labelcex=1.0,
      explode=0.1,
      radius = 1.5,
      col=rainbow(length(ds)))

# 상자그림을 이용한 정서적 지원 제도 비교 그래프
boxplot(socsupport$emotional~socsupport$country,
        main='정서적 지원 제도 비교')

boxplot(socsupport$emotional~socsupport$gender,
        main='정서적 지원 제도 비교')

boxplot(socsupport$emotionalsat~socsupport$age,
        main='정서적 지원 제도 만족도 비교',
        col=rainbow(5))

group <- as.numeric(socsupport$gender)
color <- c('blue','red')
plot(socsupport[,c('emotionalsat','tangiblesat','age')],
     pch=group,
     col=color[group])

