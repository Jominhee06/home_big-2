# 단일변수 범주형 데이터 분석
library(carData)

room.class <- TitanicSurvival$passengerClass  # 선실 정보
room.class

# 도수분포 계산
tbl <- table(room.class)
tbl
sum(tbl)   # 전체 탑승객수

# 막대그래프
barplot(tbl, main = '선실별 탑승객',
        xlab = '선실 등급',
        ylab = ' 탑승객수',
        col=c('blue','green','yellow'))

# 원 그래프
tbl/sum(tbl)
par(mar=c(1,1,4,1)) # 여백
pie(tbl, main='선실별 탑승객',
    col = c('darkblue','green','yellow'))
par(mar=c(5.1,4.1,4.1,2.1))
#_______________________________________________________________________________

# 단일변수 수치형 데이터 분석
grad <- state.x77[,'HS Grad']  # 주별 고등학교 졸업률
grad

# 사분위수
summary(grad)
var(grad)  # 분산
sd(grad)   # 표준 편차

# 히스토그램
hist(grad, main='주별 졸업률',
     xlab='졸업률',
     ylab='주의 개수',
     col='darkorange')

# 상자 그림
boxplot(grad, main = '주별 졸업률',
        col='orange')
# 졸업률이 가장 낮은 주
idx <- which(grad==min(grad))
grad[idx]

# 졸업률이 가장 높은 주
idx <- which(grad==max(grad))
grad[idx]

# 졸업률이 평균 이하인 주
idx <- which(grad<mean(grad))
grad[idx]

#_______________________________________________________________________________

# 영국 폐질환 사망자 분석 
# 데이터 준비
ds <- read.csv("D:/Rworks/fdeaths.csv", row.names='year')
ds

# 선그래프 작성
my.col <- c('black','blue','red','green','purple','darkgray')
my.lty <- 1:6

plot(1:12,                        # x data
     ds[1,],                      # y data(1974년 데이터)
     main ='월별 사망자 추이',    # 그래프 제목
     type='b',                    # 그래프 종류
     lty=my.lty[1],               # 선의 종류
     xlab='Month',                # x축 레이블
     ylab = '사망자수',           # y축 레이블
     ylim=c(300,1200),            # y축 값의 범위
     col=my.col[1]                # 선의 색
)
for(i in 2:6){
  lines(1:12, # x data            # 추가
        ds[i,],                   # y data(1975~1979)
        type='b',                 # 그래프 종류
        lty=my.lty[i],            # 선의 종류
        col=my.col[i]             # 선의 색
  )
}
legend(x= 'topright',             # 범례의 위치
       lty=my.lty,                # 선의 종류
       col=my.col,                # 선의 색
       legend = 1974:1979         # 범례의 내용
       )


