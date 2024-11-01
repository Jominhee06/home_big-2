# 방사형 차트 (레이더 차트,거미줄 차트)
install.packages('fmsb')
library(fmsb)

score <- c(80,60,95,85,40)
max.score <- rep(100,5)
min.score <- rep(0,5)
ds <- rbind(max.score,min.score,score)
ds <- data.frame(ds)
colnames(ds) <- c('국어','영어','수학','물리','음악')
ds

#방사형 차트 (매개변수의 지정)
radarchart(ds,
           pcol = 'dark green',
           pfcol=rgb(0.2,0.5,0.5,0.5),
           plwd=3,
           cglcol='grey',                 
           cglty=1,                    # 거미줄의 타입
           cglwd=0.8,                  # 거미줄의 두께
           axistype=1,
           seg=4,
           axislabcol='grey',
           caxislabels=seq(0,100,25))
#_______________________________________________________________________________

library(ggplot2)

month <- c(1,2,3,4,5,6)
rain <- c(55,50,45,50,60,70)
df <- data.frame(month,rain)
df

# 막대그래프와 히스토그램
ggplot(df, aes(x=month, y=rain)) +
  geom_bar(stat='identity',
           width = 0.7,
           fill='steelblue') +
  ggtitle('월별 강수량')+
  theme(plot.title = element_text(size=25, face = 'bold', colour='steelblue'))+
  labs(x='월', y='강수량')+
  coord_flip()

library(ggplot2)

ggplot(iris, aes(x=Petal.Length))+   # 그래프를 그릴 데이터 지정
  geom_histogram(binwidth = 0.5)     # 히스토그램 작성

ggplot(iris, aes(x=Sepal.Width, fill=Species, color=Species))+
  geom_histogram(binwidth = 0.5, position = 'dodge')+
  theme(legend.position = 'top')  # 범례의 위치
#_______________________________________________________________________________

# 산점도
library(ggplot2)

ggplot(data=iris, aes(x=Petal.Length,y=Petal.Width,
                 color=Species))+
  geom_point(size=3) +
  ggtitle('꽃잎의 길이와 폭')+
  theme(plot.title = element_text(size=25, face='bold',
colour = 'steelblue'))
#_______________________________________________________________________________

# iris 데이터 상자그림
library(ggplot2)
ggplot(data=iris, aes(y=Petal.Length))+
  geom_boxplot(fill='yellow')

library(ggplot2)
ggplot(data=iris, aes(x=Species, y=Petal.Length, fill=Species))+

geom_boxplot()


iris.new <- iris
iris.new$Species <- factor(iris.new$Species,
                           levels=c('versicolor','virginica','setosa'))

ggplot(data=iris.new, aes(x=Species, y=Petal.Length, fill=Species))+
  geom_boxplot()

#_______________________________________________________________________________

# 선 그래프
library(ggplot2)

year <- 1937:1960
cnt <- as.vector(airmiles)
df <- data.frame(year,cnt)
head(df)

ggplot(data = df, aes(x=year, y=cnt))+
  geom_point()+geom_line(col='yellow')

#_______________________________________________________________________________

# 기후 변화 그래프로 작성
head(airquality)

library(ggplot2)

df <- aggregate(airquality[,'Temp'],
                by=list(month=airquality$Month), FUN=mean)
ggplot(df, aes(x=month, y=x)) +             # 그래프를 그릴 데이터 지정
  geom_bar(stat = 'identity',               # 막대그래프의 형태 지정
           width = 0.7, fill='green')

# 상자 그림
df <- airquality[complete.cases(airquality),]  # 결측값 제거

ggplot(data=df, aes(x=factor(Month), y=Ozone,
       fill=factor(Month)))+
geom_boxplot()

# 산점도
ggplot(data=df, aes(x=Temp, y=Ozone, color='orange')) +
  geom_point(size=3)

# 선 그래프
df.7 <- subset(df,Month==7)
ggplot(data=df.7, aes(x=Day,y=Ozone)) +
  geom_line(col='red')

ggplot(data=df[df$Month==7,], aes(x=Day,y=Ozone))+
  geom_line(col='red')

#_______________________________________________________________________________

# 세계 각국의 다양한 지표 분석
library(carData)
data(UN98)
head(UN98)
help(UN98)
str(UN98)

df <- UN98[, c('region', 'tfr')]
df <- df[complete.cases(df),]
df <- aggregate(df[,'tfr'], by=list(region=df$region), FUN='mean')

ggplot(df, aes(x=region,y=x))+
  geom_bar(stat='identity',      # 막대그래프의 형태 지정
           width = 0.7, fill=rainbow(5))

library(treemap)

df <- UN98[,c('region', 'lifeFemale','illiteracyFemale')]
df <- df[complete.cases(df),]
df$country <- rownames(df)

treemap(df,
        index=c('region','country'),
        vSize = 'lifeFemale',
        vColor = 'illiteracyFemale',
        type = 'value',
        bg.labels = 'yellow',
        tltle="World's Women")


df <- UN98[,c('region', 'educationMale','educationFemale')]
df <- df[complete.cases(df),]

ggplot(data=df, aes(x=educationMale, y=educationFemale,
                    color=region)) +
  geom_point(size=3) +
  ggtitle('남성, 여성의 교육수준') +
  theme(plot.title = element_text(size=25, face='bold',
                                  colour='steelblue'))
#_______________________________________________________________________________



