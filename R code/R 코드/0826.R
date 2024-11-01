# 포브스 기업 리포트 데이터 분석

library(HSAUR)
data("Forbes2000")
ds <- Forbes2000
ds[!complete.cases(ds),]   #결측값 확인

str(ds)
head(ds)

#_______________________________________________________________________________

# 국가별 기업 통계

table(ds$country)
tmp <- sort(table(ds$country), decreasing=T)
top.10.contry <- tmp[1:10]
top.10.contry

par(mar=c(8,4,4,2))
barplot(top.10.contry,
        main='기업수 상위 10개국',
        col=rainbow(22),
        las=2
)

par(mar=c(5,4,4,2))

#_______________________________________________________________________________

# 업종별 기업 분포

table(ds$category)
tmp <- sort(table(ds$category),decreasing = T)
top.10.category <- tmp[1:10]
top.10.category

par(mar=c(10,4,4,2))
barplot(top.10.category,
        main='기업수 상위 10개 업종',
        col='pink',
        las=2)

par(mar=c(5,4,4,2))

tmp<-ds[ds$category %in% names(top.10.category),]
levels(tmp$category)

tmp$category <- factor(tmp$category)
levels(tmp$category)

par(mar=c(10,4,4,2))
boxplot(assets~category, data=tmp,
        ylim=c(0,100),
        xlab='',
        las=2)

par(mar=c(5,4,4,2))

