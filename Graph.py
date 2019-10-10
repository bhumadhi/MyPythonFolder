# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:01:52 2019

@author: bhuwan.madhikarmi
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
class Edge(object):
    def __init__(self, value, node_from, node_to):
        self. value = value
        self.node_from = node_from
        self.node_to = node_to
        
class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges= edges
        
    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            #print("inside for loop: "+ node.value)
            if node_from_val == node.value:
                #print("inside if node from present")
                from_found = node
                #print("node from found")
            if node_to_val == node.value:
                #print("inside if node to present")
                to_found = node
        if from_found == None:
            #print("node from NOT found")
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
            #print("from not found "+ str(self.nodes))
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        self.edges.append(new_edge)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
        return edge_list
    
graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()