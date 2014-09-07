#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PAA 1 algorithmic thinking course
'''

import random


def load_graph(rawdata):
	'''
	load the raw data and convet to graph
	input: raw data file name
	output: a dictionary representating the graph
	'''
	graph = {}
	f = open(rawdata)
	for line in f.readlines():
		content = line.split()
		graph[content[0]] = set(content[1:])
	return graph

# calling the function : graph = load_graph('alg_phys-cite.txt')

def compute_in_degrees(digraph):
	'''
	return degrees for each nodes in a graph
	input: a directed graph
	output: dictionary with nodes as keys and degrees as values
	'''
	# initializing a empty dictionary to store degrees
	degrees = dict()
	# set degrees all to 0
	for node in digraph:
		degrees[node] = 0
	# calculating all in degrees
	for node in degrees:
		for source_node in digraph:
			if node in digraph[source_node]:
				degrees[node] += 1
	return degrees

def in_degree_distribution(digraph):
	'''
	compute indegree distributions for a graph
	input: a directed graph
	output: dictionary with degrees as keys and count of nodes as values
	'''
	# initializing a empty dictionary to store degree distribution
	distributions = dict()
	degrees = compute_in_degrees(digraph)
	for degree in degrees.values():
		if degree not in distributions:
			distributions[degree] = 1
		else:
			distributions[degree] += 1
	return distributions

def degreeNormalization(distributions):
	'''
	normalizing a degree distributions
	input: a degree distribution calculated using in_degree_distribution
	output: a normalized degree distribution
	'''
	total = sum(distributions.values())
	for degree in distributions:
		distributions[degree] = float(distributions[degree])/total
	return distributions

def write_distributions(distributions, filename):
	'''
	function write a degree distribution to a csv file
	input: distributions calculated using in_degree_distribution(), desired target csv file name
	output: a csv file stored in the working directory
	'''
	dis_file = open(filename, 'w')
	for degree in distributions:
		dis_file.write(str(degree)+","+str(distributions[degree])+'\n')
	dis_file.close()

def ER_graph_generator(num_nodes, probability):
	'''
	generate ER graph
	input: number of notdes and the probability to generate a edge
	output: dictionary representating a generated graph
	'''
	graph = {node:set() for node in range(num_nodes)}
	for node in graph:
		for target in range(num_nodes):
			if target != node:
				p = random.random()
				if p <= probability:
					graph[node].add(target)
	return graph

def make_complete_graph(num_Nodes):
	'''
	return a full directed graph for given number of nodes
	input: number of nodes
	output: a directed graph with all possible edges
	'''
	graph = {node:set() for node in range(num_Nodes)}
	for node in graph:
		for target in range(num_Nodes):
			if node != target:
				graph[node].add(target)
	return graph

def sum_indegrees(digraph):
	'''
	helper function for DPA, calculating sum of indegrees of a graph
	input: a directed graph represented as a dictionary
	output: a interger representing the sum of indegrees
	'''
	sum_indegrees = 0
	degrees = compute_in_degrees(digraph)
	for node in degrees:
		sum_indegrees += degrees[node]
	return sum_indegrees

def DPA(n,m):
	'''

	'''
	graph = make_complete_graph(m)
	for i in range(m,n):
		print i
		indegrees = compute_in_degrees(graph)
		totindeg = sum_indegrees(graph)
		graph[i] = set()
		for node in range(i-1):
			p = random.random()
			if p < float(indegrees[node]+1)/(totindeg + len(range(i-1))):
				graph[i].add(node)
	return graph

from DPATrial import DPATrial as dpaT

def synthetic_digraph(all_nodes, existed_nodes, add):
	complete_graph = make_complete_graph(existed_nodes)
	random_connect = dpaT(existed_nodes)
	for new_node in range(existed_nodes, all_nodes):
		complete_graph[new_node] = random_connect.run_trial(add)
	distribution = in_degree_distribution(complete_graph)
	distribution.pop(0)
	return distribution

if __name__ == "__main__":
	'''
	For Question 1
	'''
	# read in the data a s a graph
	rawdata = 'alg_phys-cite.txt'
	graph = load_graph(rawdata)
	# calculating indegrees, indegree distribution
	indegrees = compute_in_degrees(graph)
	in_degree_distribution = in_degree_distribution(graph)
	# normalizing the indegree distribution
	normalized_in_degree_distribution = degreeNormalization(in_degree_distribution)
	# writing the normalized distributions to a csv file
	write_distributions(normalized_in_degree_distribution, 'distributions.csv')
	# generate plot in R
	'''
	For Question 2
	'''
	# generate a ER graph similar to the distribution and of the same size of the citation network
	ERgraph1 = ER_graph_generator(27770, 0.0005)
	ERindegrees = compute_in_degrees(ERgraph1)
	ERin_degree_distribution = in_degree_distribution(ERgraph1)
	ERnormalized_in_degree_distribution = degreeNormalization(ERin_degree_distribution)
	write_distributions(ERnormalized_in_degree_distribution, 'ERdistributions.csv')
	# generate plot in R
	'''
	For Question 3
	'''
	float(sum_indegrees(graph))/27770
	'''
	For Question 4
	'''
	# the slow way:
	g = DPA(27770,13)
	



