library(treemap)
data(GNI2014)
head(GNI2014)
treemap(GNI2014,
        index=c('continent','iso3'),  # 계층 구조 설정(대륙 - 국가)
        vSize = 'population',       # 타일 크기
        vColor = 'GNI',             # 타일 컬러
        type ='index',              # 타일 컬러링 방법 (dens , comp , index 사용)
        bg.labels = 'yellow',       # 레이블의 배경색
        title = "World's GNI")
#_______________________________________________________________________________

library(treemap)
st <- data.frame(state.x77)

# 주의 이름 열 stname을 추가
st <- data.frame(st, stname=rownames(st))

treemap(st,
        index = c('stname'),     # 타일에 주 이름 표기
        vSize = 'Area',          # 타일의 크기
        vColor = 'Income',       # 타일의 컬러
        type = 'value',          # 타일 컬러링 방법
        title = 'USA states area and income')
#_______________________________________________________________________________

library(treemap)
library(carData)
head(Ericksen)
str(Ericksen)

ds <- subset(Ericksen, city== 'state')

ds$stname <- rownames(ds)

treemap(ds,
        index=c('stname'),             # 타일에 주 이름 표기
        vSize = 'poverty',             # 타일의 크기
        vColor ='crime',               # 타일의 컬러
        type= 'value',                 # 타일 컬러링 방법
        title = 'USA states poverty and crime')

# 다중시설 거주율 그래프 그림
treemap(ds,
        index=c('stname'),                       # 타일에 주 이름 표기
        vSize = 'housing',                       # 타일의 크기
        vColor ='minority',                      # 타일의 컬러
        type= 'value',                           # 타일 컬러링 방법
        palette = heat.colors(nrow(ds)),         # 컬러 팔레트
        title = 'USA states poverty and crime')
#_______________________________________________________________________________

# 서울의 월별 기온 변화

# 1.데이터 확인
ds <- read.csv('C:/Rworks/seoul_temp_2017.csv')
dim(ds)
head(ds)

# 2.서울의 1년 기온 분포
summary(ds$avg_temp)
boxplot(ds$avg_temp,
        col='green',
        ylim=c(-20,40),
        xlab='서울 1년 기온',
        ylab='기온')

# 3. 월별 기온 분포
# 월별 평균 기온 계산
month.avg <- aggregate(ds$avg_temp,
                       by=list(ds$month),median)[2]
month.avg 

# 데이터프레임을 벡터로 변환
month.avg <- month.avg[,1]    # dataframe을 벡터로
names(month.avg) <- 1:12      # 1월~12월

# 평균기온 순위 계산 (내림차순)
odr <- rank(-month.avg)
odr

# 월별 기온 분포
boxplot(avg_temp~month, data = ds,
        col=heat.colors(12)[odr],     # 상자의 색을 지정
        ylim=c(-20,40),
        ylab='기온',
        xlab='월',
        main='서울시 월별 기온 분포(2017)')
#_______________________________________________________________________________

# 월별 오존농도 변화

# 1.데이터 확인
head(airquality)
ds <- airquality[complete.cases(airquality),]   # 결측값 제거
unique(ds$Month)                                # 월 확인

# 2.월별 오존농도 분포
# 월별 평균 오존농도 계산
month.avg <- aggregate(ds$Ozone,
                       by=list(ds$Month), median)[2]
month.avg

# 데이터프레임을 벡터로 변환
month.avg <- month.avg[,1]             # dataframe을 벡터로
names(month.avg) <- 5:9                # 5월~9월

# 평균오존농도 순위 계산(내림차순)
odr <- rank(-month.avg)
odr

# 월별 오존농도 분포
boxplot(Ozone~Month, data=ds,
        col=heat.colors(5)[odr],      # 상자의 색 지정
        ylim=c(0,170),
        ylab = '오존농도',
        xlab = '월',
        main='여름철 오존농도')

#_______________________________________________________________________________

# 캐나다 온타리오 지역의 임금 정보 분석
library(carData)
ds <- SLID[complete.cases(SLID),]
head(ds)

boxplot(wages~sex, data=ds,
        main='성별 임금',
        col=c('green','steelblue'))
        
boxplot(wages~language, data=ds,
        main='사용언어별 임금',
        col=c('green', 'steelblue','yellow'))
#_______________________________________________________________________________

# 교육연수에 따른 임금의 차이 분석 (교육 연수를 5구간)
ds$edu_group <- NA
ds$edu_group[ds$education<10] <- 'A'
ds$edu_group[ds$education>=10 & ds$education<13] <- 'B'
ds$edu_group[ds$education>=13 & ds$education<15] <- 'C'
ds$edu_group[ds$education>=15 & ds$education<18] <- 'D'
ds$edu_group[ds$education>=18] <- 'E'
boxplot(wages~edu_group, data=ds,
        main='교육기간별 임금',
        col=rainbow(5))
#_______________________________________________________________________________

# 방사형차트 (거미줄차트, 레이더차트)
install.packages('fmsb')
library(fmsb)

# 데이터 준비
score <- c(80,60,95,85,40)
max.score <- rep(100,5)         # 100을 5회 반복
min.score <- rep(0,5)           # 0을 5회 반복
ds <- rbind(max.score,min.score, score)
ds <- data.frame(ds)            # 매트릭스를 데이터프레임으로
colnames(ds) <- c('국어','영어','수학','물리','음악')
ds

# 방사형 차트
radarchart(ds)

radarchart(ds,
           pcol='dark green',
           pfcol=rgb(0.2,0.5,0.5,0.5),
           plwd=3,
           cglcol='grey',   # 거미줄의 색
           cglty = 1,       # 거미줄의 타입
           cglwd = 0.8,     # 거미줄의 두께
           axistype = 1,
           seg=4,           # 축의 눈금 분할
           axislabcol = 'grey',
           caxislabels = seq(0,100,25))

#_______________________________________________________________________________

# 종교 유무를 조사한 데이터 분석

library(carData)
head(WVS)

pop <- table(WVS$country)            # 국가별 응답자 수
tmp <- subset(WVS, religion=='yes')  
rel <- table(tmp$country)            # 국가별 종교가 있는 응답자수 
stat <- rel/pop                      # 국가별 종교가 있는 응답자수 비율 
stat

max.score <- rep(1,4)
min.score <- rep(0,4)
ds <- rbind(max.score,min.score,stat)
ds <- data.frame(ds)                  # 매트릭스를 데이터프레임으로 변환


radarchart(ds,
           pcol='dark green',
           pfcol=rgb(0.2,0.5,0.5,0.5),    # 다각형 내부색
           plwd=3,                        # 다각형 선의 두께
           cglcol='grey',                 # 거미줄의 색
           cglty=1,                       # 거미줄의 타입
           axistype = 1,
           axislabcol = 'grey',
           caxislabels = seq(0,1,0.25),
           title = '국가별 종교인 비율')
