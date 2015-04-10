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
