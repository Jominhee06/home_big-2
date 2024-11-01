# 도수분포표 계산하기
favorite <- c('WINTER','SUMMER','SPRING','SUMMER','SUMMER','FALL','FALL',
              'SUMMER','SPRING','SPRING')
favorite
table(favorite)  #도수분포 계산

# table(iris$Species)
ds <- table(favorite)
ds

barplot(ds, main = 'favorite season',
        col = 'blue',
        xlab = '계절',
        ylab = '빈도수')

barplot(ds, main = 'favorite season',
        col = c('brown','pink','plum','palegreen'),
        xlab = '계절',
        ylab = '빈도수')

barplot(ds, col = 'red')

barplot(ds, main = 'favorite season',
        col = 'green',        # 막대의 색을 지정
        horiz = TRUE)         # 수평 방향 출력

barplot(ds, main = 'favorite season',
        col = c('brown','pink','plum','palegreen'),
        names = c('FA','SP','SU','WI'))  # 그룹 이름을 바꾸어 출력

barplot(ds, main = 'favorite season',
        col = c('brown','pink','plum','palegreen'),
        las=2)                           # 수직 방향으로 
#_______________________________________________________________________________

# 중첩 그룹의 막대그래프
age.A <- c(13709,10974,7979,5000,4250)
age.B <- c(17540,29701,36209,33947,24487)
age.C <- c(991,2195,5366,12980,19007)

ds <- rbind(age.A,age.B,age.C)
colnames(ds) <- c('1970','1990','2010','2030','2050')
ds

barplot(ds, main='인구 추정',
        col = c('green','yellow','blue'))

barplot(ds, main='인구 추정',
        col = c('green','brown','blue'),
        beside =TRUE)

barplot(ds, main='인구 추정',
        col = c('green','brown','blue'),
        beside =TRUE,
        legend.text = T)

par(mfrow=c(1, 1), mar=c(5,5,5,7))   # 그래프 윈도우 설정
barplot(ds, main='인구 추정',
        col = c('green','brown','blue'),
        beside =TRUE,
        legend.text = T,
        args.legend = list(x='topright', bty='n',
                           inset=c(-0.25,0)))

par(mfrow=c(1, 1), mar=c(5,5,5,7))    # 그래프 윈도우 설정
barplot(ds, main='인구 추정',
        col = c('green','brown','blue'),
        beside =TRUE,
        legend.text = c('0~14세','15~64세','65세 이상'),
        args.legend = list(x='topright', bty='n',
                           inset=c(-0.25,0)))
par(mfrow=c(1,1),mar=c(5,4,4,2)+0.1)  # 그래프창 설정 해제

#_______________________________________________________________________________

#히스토그램
dist<-cars[,2]
dist
hist(dist,
     main ='Histogram for 제동거리',
     xlab = '제동거리',
     ylab = '빈도수',
     border = 'black',
     col='green',
     las=2,
     breaks=5)

result <- hist(dist, # data
               main='Histogram for 제동거리',
               breaks=5)

result
freq <- result$counts
names(freq) <- result$breaks[-1]
freq
#_______________________________________________________________________________

# 다중 그래프 
par(mfrow=c(2,2), mar=c(3,3,4,2))

hist(iris$Sepal.Length,
     main='Sepal.Length',
     col='orange')

barplot(table(mtcars$cyl),
        main='mtcars',
        col=c('pink','green','blue'))

barplot(table(mtcars$gear),
        main='mtcars',
        col=rainbow(3),
        horiz = TRUE)

pie(table(mtcars$cyl),
    main='mtcars',
    col=topo.colors(3),
    radius = 2)

par(mfrow=c(1,1), mar=c(5,4,4,2)+.1)


