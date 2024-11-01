cafe <- list(espresso = c(4,5,3,6,5,4,7),
             americano = c(63,68,64,68,72,89,94),
             latte = c(61,70,59,71,71,92,88),
             price = c(2.0,2.5,3.0),
             menu = c('espresso','americano','latte'))

cafe$menu <- factor(cafe$menu)

names(cafe$price) <- cafe$menu

sales.espresso <- cafe$price['espresso']* cafe$espresso
sales.americano <- cafe$price['americano']* cafe$americano
sales.latte <- cafe$price['latte']* cafe$latte

sale.day <- sales.espresso + sales.americano + sales.latte  #요일별 매출액

names(sale.day) <- c('Mon','Tue','Wed','Thu','Fri','Sat','Sun')

sum(sale.day)

sale.mean <- mean(sale.day)

names(sale.day[sale.day >= sale.mean])


accident <- c(31,26,42,47,50,54,70,66,43,32,32,22)
names(accident) <- c('M1','M2','M3','M4','M5','M6','M7','M8',
                     'M9','M10','M11','M12')
accident

sum(accident)

max(accident)
min(accident)

accident*0.9

accident[accident>=50]

month.50 <- accident[accident >= 50]
names(month.50)
names(accident[accident >= 50])

length(accident[accident<50])

M6.acc <- accident[6]
accident[accident > M6.acc]

accident[accident > accident[6]]

#_______________________________________________________________________________

#매트릭스 만들기!
z <- matrix(1:20, nrow=4, ncol=5)
z

z2 <- matrix(1:20, nrow=4, ncol=5, byrow=T)
z2

x <- 1:4
y <- 5:8
z <- matrix(1:20,nrow = 4, ncol=5)

m1 <- cbind(x,y)
m1

m2 <- rbind(x,y)
m2

m3 <- rbind(m2,x)
m3

m4 <- cbind(z,x)
m4

z <- matrix(1:20, nrow=4, ncol=5)
z

z[2,3]
z[1,4]
z[2,]
z[,4]

z[2,1:3]           # 2행의 값 중 1~3열에 있는 값
z[1,c(1,2,4)]
z[1:2,]
z[,c(1,4)]

score <- matrix(c(90,85,69,78,85,96,49,95,90,80,70,60),nrow=4)
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
colnames(score)[2]