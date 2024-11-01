library(svDialogs)
user.input <- dlgInput('Input income')$res
user.input
income <- as.numeric(user.input)
income
tax <- income * 0.05
cat('세금: ', tax)

x <- 26
y <- '입니다'
z <- c(10,20,30,40)
print(x)
print(y)
print(z)
print(iris[1:5,])
print(x,y)

cat(x,'\n')
cat(y,'\n')
cat(z,'\n')
cat(x,y,'\n')
cat(iris[1:5],'\n') # 데이터프레임 출력(에러발생)
#_______________________________________________________________________________
# 체질량 지수 계산하기

library(svDialogs)

height <- dlgInput('Input height(cm)') $res
weight <- dlgInput('Input weight(kg)') $res

height <- as.numeric(height)
weight <- as.numeric(weight)

height <- height /100
bmi <- weight/(height^2)

cat('입력한 키는 ', height*100, 'cm, 몸무게는 ', weight,'kg 입니다. \n', sep="")
cat('BMI는',bmi, '입니다.',sep="")

#_______________________________________________________________________________

getwd()
setwd('D:/Rworks') # 작업폴더 변경하기
getwd()

setwd('D:/Rworks//Rdata')
air <- read.csv('airquality.csv', header=T)
head(air)
class(air)

setwd('D:/Rworks')
my.iris <- subset(iris, Species=='setosa')
write.csv(my.iris, 'my_iris.csv', row.names=T)

install.packages('xlsx')
library(xlsx)
air <- read.xlsx('D:/Rworks/Rdata/airquality.xlsx', header=T,
                 sheetIndex=1)
head(air)
#_______________________________________________________________________________

setwd('D:/Rworks/Shiny')

library(ggplot2)
str(diamonds)

diamonds.new <- subset(diamonds, cut == 'Premium' & carat >= 2)
write.csv(diamonds.new, 'shiny_diamonds.csv', row.names = F)

diamonds.load <- read.csv('shiny_diamonds.csv', header = T)
diamonds.new <- subset(diamonds.load, color != 'D')
library(csv)
write.csv(diamonds.new, 'shiny_diamonds.csv', row.names = F)

# 실행결과를 파일로 출력하기
setwd('D:/Rworks')
print('Begin work')
a <- 10; b <- 20
sink('result.txt', append =T)    # 파일로 출력 시작
cat('a+b=' ,a+b, '\n')
sink()
cat('hello world \n')
sink('result.txt', append =T)
cat('a*b=' , a*b, '\n')
sink()
print('End work')
sink('result.txt', append =T)
cat('나는 할 수 있다!')
sink()

setwd('D:/Rworks/Rdata')
air <- read.table('airquality.txt',header = T, sep='')
head(air,3)

#_______________________________________________________________________________

library(svDialogs)
height <- dlgInput('Input height (cm) ') $res
weight <- dlgInput('Input weight (kg) ') $res
height <- as.numeric(height)
weight <- as.numeric(weight)
height <- height /100
bmi <- weight/(height^2)

sink('bmi.txt',append = T)
cat(height*100, weight, bmi)
cat('\n')
sink()

height <- dlgInput('Input height (cm) ') $res
weight <- dlgInput('Input weight (kg) ') $res

cat('\n')
sink()

# 다른이름으로 저장
result <- read.table('bmi.txt', sep=" ")
result

names(result) <- c('height', 'weight' , 'bmi')
write.table(result, 'bmi_new.txt', row.names = F)

#_______________________________________________________________________________

# 자동차 정보를 찾아 파일로 출력
library(svDialogs)
library(xlsx)
carprice.new <- read.csv('carprice.csv', header = T)
str(carprice.new)

input.type <- dlgInput('Input type')$res
input.city <- dlgInput('Input MRG.city')$res

input.city <- as.numeric(input.city)

# 2가지 조건에 만족 데이터,변수에 저장
result <- subset(carprice.new, Type == input.type & MPG.city >= input.city)

print(result)
sink('search.txt', append = T)
print(result)
sink()

# txt파일을 csv파일로 저장하기 
write.csv(result, 'search.csv',row.names = F)

#_______________________________________________________________________________







