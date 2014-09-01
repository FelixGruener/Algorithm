1 Graphs and Representation
==============================================

Example Graphs
----------------------------------------------

Undirected graph

	0-------1 
	|       |
	|       |
	3-------2

Directed graph

	0------>1
	^       |
	|       v
	3<------2

Nodes/Vertices: 
	
	V = {0,1,2,3}

Edges/Links:

	E = {{0,1},{1,2},{2,3},{3,0}} # undirected
	E = {(0,1),(1,2),(2,3),(3,0)} # directed

Representations
----------------------------------------------

Adj-List

undirected:

	undirectedAdjList = [(0,1),
	 					 (0,3),
	 					 (1,0),
	 					 (1,2),
	 					 (2,1),
	 					 (2,3),
	 					 (3,0),
	 					 (3,2)]

directed:
	
	directedAdjList = [(0,1),
	 				   (1,2),
	 				   (2,3),
	 				   (3,0)]


Adj-Matrix

undirected:

	undirectedAdjMatrix = [[0,1,0,1],
	 					   [1,0,1,0],
	 					   [0,1,0,1],
	 					   [1,0,1,0]]

directed:

	directedAdjMatrix = [[0,1,0,0],
	 				     [0,0,1,0],
	 					 [0,0,0,1],
	 					 [1,0,0,0]]


2 Degrees, Paths and Distances
==============================================

Degrees
----------------------------------------------

Degree in undirected graph:

	undirectedDegrees = {}

	# element in the dict will be:
		node: degree

	for link in undirectedAdjList:
		if link[0] not in undirectedDegrees:
	    	undirectedDegrees[link[0]] = 1
		else:
	    	undirectedDegrees[link[0]] += 1

	undirectedDegrees
	{0: 2,
	 1: 2,
	 2: 2,
	 3: 2}

	undirectedDegrees = {i:sum(undirectedAdjMatrix[i]) for i in range(len(undirectedAdjMatrix))}
	ndirectedDegrees
	{0: 2, 
	 1: 2, 
	 2: 2, 
	 3: 2}

Degree in directed graph:

	DirectedDegrees = {}

	# element in the dict will be:  
		node: [indegree, outdegree]

	for link in directedAdjList:
		if link[0] not in directedDegrees:
	    	directedDegrees[link[0]] = [0,1]
		else:
		    directedDegrees[link[0]][1] += 1
		if link[1] not in directedDegrees:
	    	directedDegrees[link[1]] = [1,0]
		else:
	    	directedDegrees[link[1]][0] += 1

	directedDegrees
	{0: [1, 1],
	 1: [1, 1],
	 2: [1, 1], 
	 3: [1, 1]}

	outdegrees = {i:sum(directedAdjMatrix[i])
	              for i in range(len(directedAdjMatrix))}
	outdegrees
	{0: 1, 1: 1, 2: 1, 3: 1}

	indegrees = {i:sum(directedAdjMatrix[j][i] for j in range(len(directedAdjMatrix)))
	             for i in range(len(directedAdjMatrix))}
	indegrees
	{0: 1, 1: 1, 2: 1, 3: 1}

	directedDegrees = {i:[sum(directedAdjMatrix[j][i] for j in range(len(directedAdjMatrix))),
						  sum(directedAdjMatrix[i])] for i in range(len(directedAdjMatrix))}.
    directedDegrees
	{0: [1, 1],
	 1: [1, 1],
	 2: [1, 1], 
	 3: [1, 1]}
						 
Paths
----------------------------------------------





