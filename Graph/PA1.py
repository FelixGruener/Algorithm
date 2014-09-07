# Representing directed graphs

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]),
			 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
			 3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
			 7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

def make_complete_graph(numNodes = None):
	# return a full directed graph for given number of nodes
	if numNodes:
		graph = {node:set() for node in range(numNodes)}
		for node in graph:
			for target in range(numNodes):
				if node != target:
					graph[node].add(target)
		return graph
	else:
		return {}	

# make_complete_graph()
# make_complete_graph(0)
# make_complete_graph(1)
# make_complete_graph(9)

# Computing degree distributions

def compute_in_degrees(digraph):
	# initializing a empty dictionary to store degrees
	degrees = dict()
	# set degrees all to 0
	for node in digraph:
		degrees[node] = 0
	# calculating all in degrees
	for node in degrees:
		for sourceNode in digraph:
			if node in digraph[sourceNode]:
				degrees[node] += 1
	return degrees

def in_degree_distribution(digraph):
	# initializing a empty dictionary to store degree distribution
	distributions = dict()
	degrees = compute_in_degrees(digraph)
	for degree in degrees.values():
		if degree not in distributions:
			distributions[degree] = 1
		else:
			distributions[degree] += 1
	return distributions

