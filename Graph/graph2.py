#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
HW2 1 algorithmic thinking course
'''

import random


def mystery(undirected_adj_matrix):
	# input: undirected graph represented as adjacency matrix
	# output: set of nodes with degree 0
	# 
	X = set()
	n = 1
	for i in range(len(undirected_adj_matrix)):
		flag = True
		n += 1
		for j in range(len(undirected_adj_matrix)):
			n += 1
			if undirected_adj_matrix[i][j] == 1:
				flag = False
				n += 1
				break
		n += 1
		if flag == True:
			X.add(i)
			n += 1
	return X,n

def BFS_Distance(graph, node):
	# input:undirected graph g, source node i
	# output: the distances node i to every nodes in graph
	queue = []
	distances = [float("Inf") for i in range(len(graph))]
	distances[node] = 0
	queue.append(node)
	while queue != []:
		j = queue.pop()
		for neighbor in graph[j]:
			if distances[neighbor] == float("Inf"):
				distances[neighbor] = distances[j] + 1
				queue.append(neighbor)
	return distances

def CC_Distance(graph):
	# input: undirected graph g
	# output the set of connected components of graph g
	RemainingNodes = graph.keys()
	ConnectedComponents = []
	while RemainingNodes != []:
		i = RemainingNodes[random.randint(0,len(RemainingNodes)-1)]
		distances = BFS_Distance(graph, i)
		component = []
		for node in RemainingNodes:
			if distances[node] != float("Inf"):
				component.append(node)
		ConnectedComponents.append(component)
		RemainingNodes = [i for i in RemainingNodes if i not in component]
	return ConnectedComponents



if __name__ == "__main__":
	Graph0 = [[0,1,1],
	          [1,0,0],
	          [1,0,0]]
	Graph1 = [[0,1.1,1],
	         [1,0,0,0],
	         [1,0,0,0],
	         [1,0,0,0]]
	Graph2 = [[0,1,1,1,1],
	          [1,0,0,0,0],
	          [1,0,0,0,0],
	          [1,0,0,0,0],
	          [1,0,0,0,0]]
	Graph3 = [[0,1,1,1,1,1],
	          [1,0,0,0,0,0],
	          [1,0,0,0,0,0],
	          [1,0,0,0,0,0],
	          [1,0,0,0,0,0],
	          [1,0,0,0,0,0]]
	X,n = mystery(Graph0)
	print n
	X,n = mystery(Graph1)
	print n
	X,n = mystery(Graph2)
	print n
	X,n = mystery(Graph3)
	print n
	
	Graph4 = [[0,0,0],
	          [0,0,0],
	          [0,0,0]]
	Graph5 = [[0,0,0,0],
	         [0,0,0,0],
	         [0,0,0,0],
	         [0,0,0,0]]
	Graph6 = [[0,0,0,0,0],
	          [0,0,0,0,0],
	          [0,0,0,0,0],
	          [0,0,0,0,0],
	          [0,0,0,0,0]]
	Graph7 = [[0,0,0,0,0,0],
	          [0,0,0,0,0,0],
	          [0,0,0,0,0,0],
	          [0,0,0,0,0,0],
	          [0,0,0,0,0,0],
	          [0,0,0,0,0,0]]
	X,n = mystery(Graph4)
	print n
	X,n = mystery(Graph5)
	print n
	X,n = mystery(Graph6)
	print n
	X,n = mystery(Graph7)
	print n

	EX_GRAPH0 = {0: set([1, 2]), 1: set([0]), 2: set([0])}
	EX_GRAPH1 = {0: set([4, 5]), 1: set([2, 6]), 2: set([1,3]),
			 3: set([2]), 4: set([0]), 5: set([0]), 6: set([1])}
	
	print "\ntest for BFS_Distance()"
	print "should be [0,1,1]"
	print(BFS_Distance(EX_GRAPH0,0))
	print "should be [1,0,2]"
	print(BFS_Distance(EX_GRAPH0,1))
	print "should be [1,2,0]"
	print(BFS_Distance(EX_GRAPH0,2))
	print "should be [0, inf, inf, inf, 1, 1, inf]"
	print(BFS_Distance(EX_GRAPH1,0))
	print "should be [inf, 0, 1, 2, inf, inf, 1]"
	print(BFS_Distance(EX_GRAPH1,1))

	print "\ntest for CC_Distance()"
	print "should be [[0,1,2]]"
	print(CC_Distance(EX_GRAPH0))
	print "should be [[1,2,3,6],[0,4,5]]"
	print(CC_Distance(EX_GRAPH1))
	



