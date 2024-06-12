# 매개변수에 기본값 설정
mydiv <- function(x,y=2){
  result <- x/y
  return(result)
}

mydiv(x=10, y=3)
mydiv(10,3)
mydiv(10)

#_______________________________________________________________________________

idx <-which(iris$Petal.Length>5.0)
idx
iris.big <- iris[idx,]
iris.big

#_______________________________________________________________________________

# 종업원의 팁 분석하기
library(reshape2)

unique(tips$sex)

idx <- which(tips[,'sex'] == 'Female')
avg.female <- mean(tips[idx, 'tip'])

idx <- which(tips[, 'sex'] == 'Male')
avg.male <- mean(tips[idx, 'tip'])

avg.female
avg.male


unique(tips$smoker)

idx <- which(tips$smoker == 'Yes')
avg.smoker <- mean(tips[idx, 'tip'])

idx <- which(tips$smoker == 'No')
avg.nosmoker <- mean(tips[idx, 'tip'])

avg.smoker
avg.nosmoker

#_______________________________________________________________________________

meanbycol.tip <- function(colname){
  value <- unique(tips[,colname])
  result <- list()
  for(i in 1:length(value)){
    idx<-which(tips[,colname] == value[i])
    result[i] <- mean(tips[idx,'tip']) 
  }
  names(result) <- value
  return(result)
}
meanbycol.tip('sex')
meanbycol.tip('smoker')

meanbycol.tip('size')
meanbycol.tip('day')

#_______________________________________________________________________________

# 도수분포표 계산하기
favorite <- c('WINTER','SUMMER','SPRING','SUMMER','SUMMER','FALL','FALL',
              'SUMMER','SPRING','SPRING')
favorite
table(favorite)

ds <- table(favorite)
ds
barplot(ds,main = 'favorite season',
        col = c('sienna1','red','pink','yellow'))

barplot(ds,main = 'favorite season',
        col = rainbow(4), # 레인보우 팔레트에서 4개의 색 선택
        xlab = '계절',    # x축 설명
        ylab = '빈도수')  # y축 설명

barplot(ds,main = 'favorite season',
        col = 'yellow',
        horiz = TRUE)   # 수평 방향으로 출력

barplot(ds,main = 'favorite season',
        col = 'green',
        names=c('FA','SP','SU','WI'))  # 그룹 이름을 변경

barplot(ds,main = 'favorite season',
        col = 'green',
        las=2)        # 그룹 이름을 수직 방향으로

# 막대그래프 색상 종류
colors()


# 중첩 막대그래프
age.A <- c(13709,10974,7979,5000,4250)
age.B <- c(17540,29701,36209,33947,24487)
age.C <- c(991,2195,5366,12980,19007)

ds <- rbind(age.A,age.B,age.C)
colnames(ds) <- c('1970','1990','2010','2030','2050')
ds

# o는 테두리 표시 , n은 테두리 표시 안함
par(mfrow=c(1,1),mar=c(5,5,5,7))
barplot(ds, main='인구 추정',
        col=c('green','blue','yellow'),
        beside=TRUE,   # 차트 구분
        legend.text = c('0~14세','15~64세','65세 이상'),
        #legend.text = T, # 범례 추가 
        args.legend = list(x='topright',bty='n',
                           inset=c(-0.25,0)))
par(mfrow=c(1,1), mar=c(5,4,4,2)+0.1)  # 그래프창 설정 해제

#_______________________________________________________________________________

# 사업부문별 매출액 그래프 
ha <- c(54659,61028,53307,46161,54180)
he <- c(31215,29863,32098,39684,29707)
mc <- c(15104,16133,15222,13208,9986)
vs <- c(13470,14231,13401,13552,13193)
bs <- c(16513,14947,15112,14392,17091)

ds <- rbind(ha,he,mc,vs,bs)
colnames(ds) <- c('19.1Q','19.2Q','19.3Q','19.4Q','20.1Q')
ds


par(mfrow=c(1,1), mar=c(5,4,4,10))
barplot(ds, main = '사업부문별 매출액',
        col =c('#003f5c','#58508d','#bc5090','#ff6361','#ffa600'),
        horiz=T, las = 1,
        xlab = '억 원', beside = T,
        #legend.text = T,
        legend.text = c('H&A','HE','MC','VS','BS'),
        args.legend = list(x='topright', bty='n', inset =c(-0.25,0)))

par(mfrow=c(1,1), mar=c(5,4,4,2)+.1)

#_______________________________________________________________________________

# 히스토그램
head(cars)
dist <- cars[,2]
dist
hist(dist,
     main = 'Histogram for 제동거리',
     xlab = '제동거리',
     ylab = '빈도수',
     border = 'black',
     col = 'darkgreen',
     las= 2,   # x축 글씨 방향(0~3)
     breaks=6) # 막대 개수 조절

result <- hist(dist, # data
               main = 'Histogram for 제동거리',
               breaks =5)
result
freq <- result$counts   # 구간별 빈도수 저장
names(freq) <- result$breaks[-1]  # 구간값을 이름으로 지정
freq                    # 구간별 빈도수 출력

#_______________________________________________________________________________

# 다이아몬드 시세 파악하기
library(Stat2Data)
data(Diamonds)
ds <- Diamonds$PricePerCt

color <- rep('#a8dadc', 9)
color[3] <- '#1d3557'

hist(ds, main = '1캐럿당 가격 분포',
     breaks = 9,
     xlab = '캐럿당 가격($)', ylab='빈도수', las =1,
     col = color,
     border = '#457b9d')

par(mfrow=c(2,2), mar=c(3,3,4,2))

hist(iris$Sepal.Length,
     main = 'Sepal.Length',
     col = 'orange')

barplot(table(mtcars$cyl),
        main='mtcars',
        col = c('red','green','blue'))

barplot(table(mtcars$gear),
        main='mtcars',
        col = rainbow(3),
        horiz = T)

pie(table(mtcars$cyl),
    main = 'mtcasr',
    col = topo.colors(3),  # topo 팔레트 사용
    radius = 2)

par(mfrow=c(1,1), mar=c(5,4,4,2)+.1)

#_______________________________________________________________________________

# 정책 지지도 그래프 그리기
install.packages('carData')
library(carData)
ds <- Chile
colors<-rainbow(20)

par(mfrow = c(2,3))

barplot(table(ds$region), main ='지역별 분포', col=colors[1:5])
barplot(table(ds$sex), main ='성별 분포', col=colors[6:7])
barplot(table(ds$education), main ='교육수준별 분포', col=colors[8:10])

hist(ds$age, breaks=6, main='연령', xlab = 'age', col=colors[1:6])
hist(ds$income, breaks=4, main='수입', xlab='income',
     col=colors[11:14])
hist(ds$statusquo, breaks=9, main='정책 지지도', xlab='swpport',
     col=colors[15:20])
#_______________________________________________________________________________

# 종업원의 팁 정보 그래프 작성 
library(reshape2)
str(tips)

par(mfrow = c(2,2))
barplot(table(tips$sex), main = 'gender')
barplot(table(tips$day), main = 'Day of the week')
barplot(table(tips$time), main = 'time')
barplot(table(tips$size), main = 'size')
par(mfrow = c(1,1))

color.6 <- rep('#a8dadc',6)
color.6[2] <- '#1d3357'
color.4 <- rep('#a8dadc',4)

color.4[2] <- '#1d3557'
color.4[3] <- '#457b9d'
par(mfrow = c(2,2))

# 막대에 색 강조
barplot(table(tips$sex), main = 'gender',col = c('#a8dadc','#1d3557'))
barplot(table(tips$day), main = 'Day of the week',col=color.4)
barplot(table(tips$time), main = 'time',col=c('#1d3557','#a8dadc'))
barplot(table(tips$size), main = 'size',col=color.6)
par(mfrow = c(1,1))

tips.new <- tips
tips.new$perHead <- tips.new$total_bill / tips.new$size

color.5 <- rep('#a8dadc',6)
color.5[2] <- '#1d3357'

par(mfrow = c(1,3))
hist(tips.new$perHead, main = '1인당 주문 금액', breaks = 5,
     xlab ='단위 :달러',
     col = color.5)
hist(tips.new[tips.new$time == 'Lunch','perHead'],
     main = '1인당 주문 금액(런치)', breaks= 4, xlab = '단위: 달러',
     col = color.5)
hist(tips.new[tips.new$time == 'Dinner', 'perHead'],
  main = '1인당 주문 금액(디너)', breaks = 4, xlab = '단위:달러',
  col= color.5)
par(mfrow =c(1,1))


# 주문금액 대비 받은 팁 비율
tips.new$percent <- tips.new$tip / tips.new$total_bill * 100
par(mfrow = c(1,2))
res.lunch <- hist(tips.new[tips.new$time == 'Lunch', 'percent'],
                  main = '주문 금액 대비 팁의 비율(런치)',
                  xlab = 'percent(%)',
                  breaks = 5)
res.dinner <- hist(tips.new[tips.new$time == 'Dinner', 'percent'],
                   main = '주문 금액 대비 팁의 비율(디너)',
                   xlab = 'percent(%)',
                   breaks = 10)
par(mfrow = c(1,1))

