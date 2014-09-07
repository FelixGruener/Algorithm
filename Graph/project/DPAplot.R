library(ggplot2)

distribution <- read.csv('ERdistributions.csv')
names(distribution) <- c('indegree','probability')


png("ERdistribution.png", width = 800, height = 600)
qplot(indegree,probability,data=distribution,log="xy",
      xlab = 'number of links', ylab = 'probability of a node',
      main = 'ER distribution (n = 27770, p = 0.0005)' )
dev.off()