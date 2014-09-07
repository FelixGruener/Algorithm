def Undirected_AdjList_Degrees(undirectedAdjList, numNodes = None):
	undirectedDegrees = {}
	if numNodes == None:
		numNodes = len(set(undirectedAdjList[i][0] for i in range(len(undirectedAdjList))))
	for link in undirectedAdjList:
		if link[0] not in undirectedDegrees:
			undirectedDegrees[link[0]] = 1
		else:
			undirectedDegrees[link[0]] += 1
	if numNodes != len(undirectedDegrees):
		for i in range(numNodes):
			if i not in undirectedDegrees.keys():
				undirectedDegrees[i] = 0
	return undirectedDegrees


def Directed_AdjList_Degrees(directedAdjList, numNodes = None):
	directedDegrees = {}
	if numNodes == None:
		numNodes = len(set(directedAdjList[i][j] for j in range(2) for i in range(len(directedAdjList))))
	for link in directedAdjList:
		if link[0] not in directedDegrees:
			directedDegrees[link[0]] = [0,1]
		else:
			directedDegrees[link[0]][1] += 1
		if link[1] not in directedDegrees:
			directedDegrees[link[1]] = [1,0]
		else:
			directedDegrees[link[1]][0] += 1]
	if numNodes != len(directedDegrees):
		for i in range(numNodes):
			if i not in directedDegrees.keys():
				directedDegrees[i] = [0,0]
	return directedDegrees


def Undirected_AdjMatrix_Degrees(undirectedAdjMatrix):
	return {i:sum(undirectedAdjMatrix[i]) for i in range(len(undirectedAdjMatrix))}


def Directed_AdjMatrix_Degrees(directedAdjMatrix):
	return {i:[sum(directedAdjMatrix[j][i] for j in range(len(directedAdjMatrix))),
			 sum(directedAdjMatrix[i])] for i in range(len(directedAdjMatrix))}


def degrees(graph, Matrix = True, Directed = True, numNodes = None):
	degrees = {}
	if Matrix == True and Directed == True:
		return Directed_AdjMatrix_Degrees(graph)
	if Matrix == True and Directed == False:
		return Undirected_AdjMatrix_Degrees(graph)
	if Matrix == False and Directed == False:
		return Undirected_AdjList_Degrees(graph, numNodes)
	if Matrix == False and Directed == True:
		return Directed_AdjList_Degrees(graph, numNodes)


def degreeNormalization(distributions):
	total = sum(distributions.values())
	for degree in distributions:
		distributions[degree] = float(distributions[degree])/total
	return distributions


def degree_distribution_undirected(degrees):
	distributions = {}
	for degree in degrees:
		if degrees[degree] not in distributions:
			distributions[degrees[degree]] = 1
		else:
			distributions[degrees[degree]] += 1
	distributions = degreeNormalization(distributions)
	return distributions


def degree_distribution_directed(degrees):
	inDegreeDistributions = {}
	outDegreeDistributions = {}
	for degree in degrees:
		if degrees[degree][0] not in inDegreeDistributions:
			inDegreeDistributions[degrees[degree][0]] = 1
		else:
			inDegreeDistributions[degrees[degree][0]] += 1
		if degrees[degree][1] not in outDegreeDistributions:
			outDegreeDistributions[degrees[degree][1]] = 1
		else:
			outDegreeDistributions[degrees[degree][1]] += 1
	inDegreeDistributions = degreeNormalization(inDegreeDistributions)
	outDegreeDistributions = degreeNormalization(outDegreeDistributions)
	return inDegreeDistributions, outDegreeDistributions


def degree_distribution(degrees, Directed = True):
	if Directed == True:
		return degree_distribution_directed(degrees)
	if Directed == False:
		return degree_distribution_undirected(degrees)


if __name__ == "__main__":
	# undirectedAdjList = [(0,1), (0,3), (1,0), (1,2), (2,1), (2,3), (3,0), (3,2)]
	# directedAdjList = [(0,1), (1,2), (2,3), (3,0)]
	# undirectedAdjMatrix = [[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
	# directedAdjMatrix = [[0,1,0,0], [0,0,1,0], [0,0,0,1], [1,0,0,0]]
	# print degrees(undirectedAdjList, Matrix = False, Directed = False)
	# print degrees(undirectedAdjList, Matrix = False, Directed = False, numNodes = 8)
	# print degrees(directedAdjList, False, True)
	# print degrees(undirectedAdjMatrix, True, False)
	# print degrees(directedAdjMatrix, True, True)
	# print degree_distribution(degrees(undirectedAdjList, Matrix = False, Directed = False), Directed = False)
	# print degree_distribution(degrees(directedAdjList, False, True), True)
	Graph1Matrix = [[0,1,0,0,1,0,1,0],
					[1,0,1,0,0,0,1,0],
					[0,1,0,1,0,0,1,0],
					[0,0,1,0,0,0,1,0],
					[1,0,0,0,0,1,0,0],
					[0,0,0,0,1,0,0,0],
					[1,1,1,1,0,0,0,0],
					[0,0,0,0,0,0,0,0]]
    print Graph1Matrix[2][6]
    Graph1Degrees = degrees(Graph1Matrix, Matrix = True, Directed = False)
    print degree_distribution(Graph1Degrees, Directed = False)
    Graph2Matrix = [[0,1,0,0,1,1,0,0],
    				[0,0,1,0,0,0,1,0],
    				[0,0,0,1,0,0,0,1],
    				[1,0,0,0,0,0,0,1],
    				[0,1,0,0,0,0,0,0],
    				[0,0,1,0,0,0,0,0],
    				[0,0,0,0,0,0,0,0],
    				[0,0,0,1,1,0,0,0]]
    Graph2Degrees = degrees(Graph2Matrix, D irected = True)
    for node in Graph2Degrees:
    	print Graph2Degrees[node]
    print Graph2Matrix[2][1]








