library(ggplot2)

distribution <- read.csv('distributions.csv')
names(distribution) <- c('indegree','probability')


png("distribution.png", width = 800, height = 600)
qplot(indegree,probability,data=distribution,log="xy",
      xlab = 'number of citation', ylab = 'probability of a paper',
      main = 'citation distribution' )
dev.off()