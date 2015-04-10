setwd("~/Documents/python/python_practice/airlines")
airlines <- read.csv("CA.csv", header = T)
airlines$CA <- rep("yes", nrow(airlines))

MU <- read.csv("MU.csv", header = T)
res <- merge(airlines, MU, by="ICAO", all.x = T, all.y = T)
