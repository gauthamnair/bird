library(ggplot2)
library(dplyr)
library(magrittr)

x <- read.csv("mitfcu.csv", header=TRUE)

x <- transform(x, day = as.Date(Date, "%m/%d/%Y"))

flipped <- x[order(nrow(x):1),]

q <- ggplot(flipped, aes(x=day, y = Balance))  + geom_step()
print(q)

smallTrend <- flipped %>%
    transform(change = 
        ifelse(!is.na(Amount.Debit), Amount.Debit, 0) + 
        ifelse(!is.na(Amount.Credit), Amount.Credit, 0)) %>%
    subset(abs(change) < 1000) %>%
    transform(smallSpend = cumsum(change))

q <- ggplot(smallTrend, aes(x=day, y = smallSpend))  + geom_step()
print(q)
