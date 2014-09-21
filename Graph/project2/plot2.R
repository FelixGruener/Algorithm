library(ggplot2)

time <- read.table('time.txt')
fast_time <- read.table('fast_time.txt')
number_of_nodes <- as.vector(rep(seq(10,990,10),2))
run_time <- as.vector(rbind(time, fast_time))
algorithm <- as.vector(c(rep('targeted_order',99),rep('fast_targeted_order',99)))

df <- as.data.frame(cbind(number_of_nodes,run_time,algorithm))
png("plot2.png", width = 800, height = 600)
ggplot(df, aes(x = number_of_nodes, y = V1)) +
  geom_line(aes(group = algorithm, color= algorithm), size = 1, aplha = 0.5) +
  labs(title = "desktop Python algorithm runtime", 
       x= "Number of Nodes in UPA graph", 
       y = "Time to generate attack order")
dev.off()