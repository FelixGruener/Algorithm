#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PA2 for algorithmic thinking course
'''

import random

# Breadth-first search

def bfs_visited(ugraph, start_node):
	# input: undirected graph represented as adj list, a starting node
	# output: a set containing the nodes connected to the starting node
	queue = [start_node]
	visited = [start_node]
	while queue != []:
		node = queue.pop()
		for neighbor in ugraph[node]:
			if neighbor not in visited:
				visited.append(neighbor)
				queue.append(neighbor)
	return set(visited)
# test 
# EX_GRAPH1 = {0: set([4, 5]), 1: set([2, 6]), 2: set([1,3]), 3: set([2]), 4: set([0]), 5: set([0]), 6: set([1])}
# bfs_visited(EX_GRAPH1,0)


# Connected components
def cc_visited(ugraph):
	# input: undirected graph represented as adj list
	# output: list of sets, each set represents a connected component
	remaining_nodes = ugraph.keys()
	connected_components = []
	while remaining_nodes != []:
		node = remaining_nodes[random.randint(0,len(remaining_nodes)-1)]
		component = bfs_visited(ugraph, node)
		connected_components.append(component)
		remaining_nodes = [remain for remain in remaining_nodes if remain not in component]
	return connected_components

# cc_visited(EX_GRAPH1)

# Largest Connected component size
def largest_cc_size(ugraph):
	# input: undirected graph represented as adj list
	# output: integer representing the size of the largest connected component
	connected_components = cc_visited(ugraph)
	length = [len(component) for component in connected_components]
	if length == []:
		return 0
	return max([len(component) for component in connected_components])

# largest_cc_size(EX_GRAPH1)	

# Graph resilience

def compute_resilience(ugraph, attack_order):
	# input: undirected graph represented as adj list, list of nodes to be removed from graph
	# output, list of the size of the largest connected component in the remaining graph
	remaining_largest_cc_size = [largest_cc_size(ugraph)]
	for node in attack_order:
		ugraph.pop(node)
		for edge in ugraph.values():
			edge.discard(node)
		remaining_largest_cc_size.append(largest_cc_size(ugraph))
	return remaining_largest_cc_size

# compute_resilience(EX_GRAPH1, [0,1])



