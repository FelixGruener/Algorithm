#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PAA 2 algorithmic thinking course
'''

import random
import time
import math

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)\
        order.append(max_degree_node)
    return order
    
def load_graph(graph_file):
    """
    Function that loads a graph for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = open(graph_file)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[:-1]
    print "Loaded graph with", len(graph_lines), "nodes"
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
    return answer_graph

def undirected_ER_graph_generator(num_nodes, probability):
    '''
    generate a undirected ER graph
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
                    graph[target].add(node)
    return graph

if __name__ == "__main__":
    graph_file = 'alg_rf7.txt'
    graph = load_graph(graph_file)
