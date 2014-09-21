library(ggplot2)

resiliences <- as.vector(read.table('graph_resiliences.txt'))
erresiliences <- as.vector(read.table('ergraph_resiliences.txt'))
uparesiliences <- as.vector(read.table('upagraph_resiliences.txt'))
number_of_nodes_removed <- as.vector(c(seq(0,1347),
                                       seq(0,1347),
                                       seq(0,1347)))
resilience <- as.vector(rbind(resiliences,erresiliences,uparesiliences))
graph <- as.vector(c(rep('computer_network',1348),
                     rep('er p=0.001716433045422606',1348),
                     rep('upa m =2',1348)))

df <- as.data.frame(cbind(number_of_nodes_removed,resilience,graph))

png("plot1.png", width = 800, height = 600)
ggplot(df, aes(x = number_of_nodes_removed, y = V1)) +
  geom_line(aes(group = graph, color= graph), size = 1, aplha = 0.5) +
  labs(title = "Network Resiliences", 
       x= "Number of Nodes Removed", 
       y = "Size of the Largest Connected Component")
dev.off()