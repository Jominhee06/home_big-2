# 포브스 기업 데이터 분석
install.packages('HSAUR')
library(HSAUR)
data("Forbes2000")
ds <- Forbes2000
ds[!complete.cases(ds),]  # 결측값 확인
str(ds)
head(ds)
#________________________________________________________________________

# 업종별 기업 분포
table(ds$country)
tmp <- sort(table(ds$country), decreasing = T)
top.10.contry <- tmp[1:10]
top.10.contry

par(mar=c(8,4,4,2))    # 그래프 여백
barplot(top.10.contry,
        main = '기업수 상위 10개국',
        col = rainbow(10),
        las=2
)
par(mar=c(5,4,4,2))

# 업종별 기업자산 분포
table(ds$category)
tmp <- sort(table(ds$category), decreasing = T)
top.10.category <- tmp[1:10]
top.10.category

par(mar=c(10,4,4,2))    # 그래프 여백
barplot(top.10.category,
        main = '기업수 상위 10 업종',
        col = 'pink',
        las=2
)
par(mar=c(5,4,4,2))

# 업종별 기업자산 분포 (박스플롯)
tmp <- ds[ds$category %in% names(top.10.category),]
levels(tmp$category)
tmp$category <- factor(tmp$category)
levels(tmp$category)

par(mar=c(10,4,4,2))   # 그래프 여백
boxplot(assets~category, data = tmp,
        ylim =c(0,100),
        xlab='',
        las=2)
par(mar=c(5,4,4,2))
#________________________________________________________________________

# 기업 가치 상위 10대 기업
tmp <- ds[order(ds$marketvalue, decreasing = T),]
tmp[1:10,c('name', 'country', 'category', 'marketvalue')]

# 한국 기업 정보
korea <- subset(ds, country=='South Korea')
korea[,c('rank','name','category','marketvalue')]
tmp <- korea[order(ds$marketvalue, decreasing = T),]
tmp[1:10,c('name', 'country', 'category', 'marketvalue')]
#________________________________________________________________________

# 기업 가치와 타 변수와의 상관관계
tmp <- ds[,5:8]
tmp <- tmp[complete.cases(tmp),]
plot(tmp,lower.panel=NULL)  # 산점도
cor(tmp)   # 상관계수

#________________________________________________________________________

# 대기오염 측정 데이터 분석
setwd('C:/Rworks')
files <- c('ds.2015.csv','ds.2016.csv','ds.2017.csv',
           'ds.2018.csv','ds.2019.csv')

ds <- NULL
for (f in files) {
  tmp <- read.csv(f, header=T)
  ds <- rbind(ds, tmp)
  print(f)
}

str(ds)
head(ds)
unique(ds$loc)   # 관측 장소
range(ds$mdate)  # 측정 기간


# 열별 결측값 확인
for( i in 3:8){
    cat(names(ds)[i], sum(is.na(ds[,i])),
sum(is.na(ds[,i]))/nrow(ds), '\n')
}
ds <- ds[,-8]                  # PM25 열 제거
ds <- ds[complete.cases(ds),]  # 결측값 포함 행 제거


# 그룹 정보 추가
mdate <- as.character(ds$mdate)
head(mdate)
ds$year <- as.numeric(substr(mdate, 1,4))
ds$month <- as.numeric(substr(mdate, 5,6))
ds$hour <- as.numeric(substr(mdate, 9,10))
ds$locname <- NA                       # locname 열을 추가
ds$locname[ds$loc==111123] <- '서울'
ds$locname[ds$loc==336111] <- '목포'
ds$locname[ds$loc==632132] <- '강릉'

head(ds)


# 지역별 PM10 농도 분포
boxplot(PM10~locname, data=ds,
        main = '미세먼지 농도 분포')
boxplot(PM10~locname, data=ds,
        main = '미세먼지 농도 분포',
        ylim=c(1,100))


# 연도별, 지역별 PM10 농도 추이
library(ggplot2)

tmp.year <- aggregate(ds[,7],
by=list(year=ds$year,loc=ds$locname), FUN='mean')
tmp.year$loc = as.factor(tmp.year$loc)
head(tmp.year)

ggplot(tmp.year, aes(x=year,y=x, colour=loc, group=loc))+
  geom_line()+
  geom_point(size=6, shape=19, alpha=0.5)+
  ggtitle('연도별 PM10 농도 변화')+
  ylab('농도')


# 월별, 지역별 PM10 농도 추이
tmp.month <- aggregate(ds[,7],
by=list(month=ds$month,loc=ds$locname), FUN='mean')
tmp.month$loc = as.factor(tmp.month$loc)
head(tmp.month)

ggplot(tmp.month, aes(x=month,y=x, colour=loc, group=loc))+
  geom_line()+
  geom_point(size=3, shape=19, alpha=0.5)+
  ggtitle('월별 PM10 농도 변화')+
  ylab('농도')


# 시간대별,지역별 PM10 농도 추이
tmp.hour <- aggregate(ds[,7],
by=list(hour=ds$year,loc=ds$locname), FUN='mean')
tmp.hour$loc = as.factor(tmp.hour$loc)
head(tmp.hour)

ggplot(tmp.hour, aes(x=hour,y=x, colour=loc, group=loc))+
  geom_line()+
  geom_point(size=3, shape=19, alpha=0.5)+
  ggtitle('시간별 PM10 농도 변화')+
  ylab('농도')


# 오염물질 농도 간의 상관관계
set.seed(1234)
plot(ds[sample(nrow(ds),5000),3:7], lower.panel=NULL)
cor(ds[,3:7])


# 미세먼지 최고점과 최저점 확인
tmp.yml <- aggregate(ds[,7],
                     by=list(year=ds$year,month=ds$month,
                             loc=ds$locname),FUN='mean')


# 가장 미세먼지가 많았던 달
idx <- which(tmp.yml$x==max(tmp.yml$x))
tmp.yml[idx,]


# 가장 미세먼지가 적었던 달
idx <- which(tmp.yml$x==min(tmp.yml$x))
tmp.yml[idx,]