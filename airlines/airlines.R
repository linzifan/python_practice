setwd("~/Documents/python/python_practice/airlines")
CA <- read.csv("CA.csv", header = T)
CA$CA <- "yes"
MU <- read.csv("MU.csv", header = T)
MU$MU <- "yes"
CZ <- read.csv("CZ.csv", header = T)
CZ$CZ <- "yes"
HU <- read.csv("HU.csv", header = T)
HU$HU <- "yes"
allairline <- merge(CA[, c(3,6)], MU[, c(3,6)], by = "IATA", all = TRUE)
allairline <- merge(allairline, CZ[, c(3,6)], by = "IATA", all = TRUE)
allairline <- merge(allairline, HU[, c(3,6)], by = "IATA", all = TRUE)

allairline <- read.csv("all_destinations_modified.csv", header = T)
summary(allairline$Country[allairline$CA != "NULL"])
bplt <- barplot(sort(summary(allairline$Country), decreasing = TRUE),  
                beside=TRUE, horiz=TRUE)
names(sort(summary(allairline$Country), decreasing = TRUE))
# variable 'bplt' is now a matrix of vertical bar positions on the y-axis

text(x= sort(summary(allairline$Country), decreasing = TRUE)+0.3, y= bplt, 
     labels=sort(summary(allairline$Country), decreasing = TRUE), xpd=TRUE)