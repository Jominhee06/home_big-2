d <- c(1,4,3,7,8)
2*d
d-5
3*d + 4
d[c(1,3,5)]
d[1:3]          # 1,2,3번째 출력
d[seq(1,5,2)]
d[-2]           #-는 '제외하고'의 의미
d[-c(3:5)]

sales <- c(640,720,680,540)              # 1~4월 매출액
names(salse)<-c('M1','M2','M3','M4')     # 매출액에 월을 이름으로 붙임
sales                                    # 1~4월 매출액 출력
sales[1]                                 # 1월 매출액 출력
sales['M2']                              # 2월 매출액 출력
sales[c('M1','M4')]                      # 1월,4월 매출액 출력

customer <- c('kim','lee','park','choi','seo')
deposit <- c (5000000,4500000,4000000,5500000,6000000)
rate <- c(3.5,3,4,5,4.5)
period <- c(2,2,5,7,4)
names(deposit) <- customer
names(rate) <- customer
names(period) <- customer

who <- customer

sum <- deposit[who] *(1 + rate[who] / 100) ^ period[who]
sum

d <- c(1,7,4,2,3)        # 벡터 d에 5개의 값을 저장
sort(d)                  # 벡터 d의 값들을 오름차순으로 정렬하여 출력
sort(d,decreasing=TRUE)  # 벡터 d의 값들을 내림차순으로 정렬

sort(x=d, decreasing = FALSE)   # 정식 문법
sort(x=d)                       # 선택적 매개변수의 생략
sort(d)                         # 매개변수명의 생략

str <- paste('good','morning', sep=' / ')
srt

paste0(1:12)
paste(1:12)        # same
as.character(1:12) # same

## If you pass several vectors to paste0, they are concatenated in a
## vectorized way.
(nth <- paste0(1:12, c("st", "nd", "rd", rep("th", 9))))

## paste works the same, but separates each input with a space.
## Notice that the recycling rules make every input as long as the longest input.
paste(month.abb, "is the", nth, "month of the year.")
paste(month.abb, letters)

## You can change the separator by passing a sep argument
## which can be multiple characters.
paste(month.abb, "is the", nth, "month of the year.", sep = "_*_")

## To collapse the output into a single string, pass a collapse argument.
paste0(nth, collapse = ", ")

## For inputs of length 1, use the sep argument rather than collapse
paste("1st", "2nd", "3rd", collapse = ", ") # probably not what you wanted
paste("1st", "2nd", "3rd", sep = ", ")

a <- '나의 나이는'
b <- 20
c <- '입니다'
paste(a,b,c, sep=' ')

a <- 1:12
b <- '월'
c <- paste(a,b, sep='')
c
#________________________________________________________________________________

sales <-c(750,740,760,680,700,710,850,890,700,720,690,730)
names(sales)<-paste(1:12, '월', sep="")
sales

sales['7월']

sales['1월']+sales['2월']

max.month <- sort(sales,decreasing = T)
max.month[1]

sum(sales[1:6])

x <- c(1,2,3,4)
y <- c(5,6,7,8)
x + y
x * y
z <- x + y
z

m <- c(x,y)
m
n <- c(y,x)
n
p <- c(x,y,90,100)
p

#________________________________________________________________________________

v1 <- c(1,2,3,4)
v2 <- c('John','Jane','Tom')
v3 <- c(v1,v2)            # v1,v2의 원소들을 결합하여 v3에 저장
v3

d <- c(1,2,3,4,5,6,7,8,9,10)
sum(d)
sum(2*d)
length(d)
mean(d[1:5])
max(d)
min(d)
sort(d)                       # 오름차순 정렬
sort(d, decreasing = FALSE)   # 오름차순 정렬
sort(d, decreasing = TRUE)    # 내림차순 정렬

v1 <- median(d)
v1
v2 <- sum(d)/length(d)
v2
#_______________________________________________________________________________

d <- 1:9
d>5        
d[d>5]
sum (d>5)
sum(d[d>5])
d==5

condi <- d > 5 & d < 8
d[condi]

condi

#_______________________________________________________________________________

espresso <- c(4, 5, 3, 6, 5, 4, 7)
americano <- c(63, 68, 64, 68, 72, 89, 94)
latte <- c(61,70,59,71,71,92,88)

sale.espresso <- 2 * espresso
sale.americano <- 2.5 * americano
sale.latte <- 3.0 * latte

sale.day <- sale.espresso + sale.americano + sale.latte
names(sale.day)<- c ('Mon','Tue','Wed','Thu','Fri','Sat','Sun')

sum(sale.day)

sale.mean <- mean(sale.day)

sum(sale.mean)

(sale.day[sale.day >= sale.mean])

#_______________________________________________________________________________

bt <- c('A','B','B','O','AB','A')
bt.new <- factor(bt)
bt
bt.new
bt[5]
bt.new[5]
levels(bt.new)
as.integer(bt.new)
bt.new[7] <- 'B'
bt.new[8] <- 'C'
bt.new  

#________________________________________________________________________________

h.list <- c('balling','tennis','skt')
person<- list(name = 'Tom',age=25, student=TRUE,hobby=h.list)
person
person[[1]]
person$name
person[[4]][3]

#________________________________________________________________________________

# 카페메뉴를 리스트를 활용하여 입력!
cafe <- list(espresso = c(4,5,3,6,5,4,7),
             americano = c(63,68,64,68,72,89,94),
             latte = c(61,70,59,71,71,92,88),
             price = c(2.0,2.5,3.0),
             menu = c('espresso','americano','latte'))

# 카페메뉴 <- 펙터로 변경! 
cafe$menu <- factor(cafe$menu)

names(cafe$price) <- cafe$menu

sale.espresso <- cafe$price['espresso']*cafe$espresso
sale.americano <- cafe$price['americano']*cafe$americano
sale.latte <- cafe$price['latte']*cafe$latte

#요일별 매출액
sale.day <- sale.espresso + sale.americano + sale.latte
names(sale.day) <- c('Mon','Tue','Wed','Thu','Fri','Sat','Sun')

#카페메뉴 요일별 총 매출액!
sum(sale.day)

#평균 매출액
sale.mean <- mean(sale.day)

sum(sale.mean)

(sale.day[sale.day >= sale.mean])

mames(sale.day[sale.day >= sale.mean])

