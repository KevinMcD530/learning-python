# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:39:31 2016

@author: kmcdonal
"""
import matplotlib.pyplot as plt
import directed_graph_representation as core_code
import random

class AlgorithmER_undirected:
    ''' Algorithm to create undirected graphs represented by a dictionary of nodes
    and edges'''
    
    def __init__(self, num_nodes, p):
        self.num_nodes = num_nodes
        self.probability = p
        self.graph_dict = {}
        self.graph_keys = range(num_nodes)
        for item in self.graph_keys:
            self.graph_dict[item] = set([])
        
    def return_keys(self):
        return self.graph_keys
        
    def return_num_nodes(self):
        return self.num_nodes
        
    def return_edge_prob(self):
        return self.probability
        
    def get_graph(self):
       return self.graph_dict

    def get_edges(self):
        return self.graph_dict.values()
        
       
    def create_edges(self):
        for item1 in self.graph_keys:
           for item2 in self.graph_keys:
               #print "Looking at :" , item1
               if item1 == item2 or set([item2]).issubset(self.graph_dict[item1]) == True:
                   pass

               else:
                   a = random.random()
                   if a < self.probability:
                       self.graph_dict[item1].add(item2)
                       self.graph_dict[item2].add(item1)
                       print "1 Loop of generated edges complete"
        return self.graph_dict


class AlgorithmER_directed:
    ''' Algorithm to create undirected graphs represented by a dictionary of nodes
    and edges'''
    
    def __init__(self, num_nodes, p):
        self.num_nodes = num_nodes
        self.probability = p
        self.graph_dict = {}
        self.graph_keys = range(num_nodes)
        for item in self.graph_keys:
            self.graph_dict[item] = set([])
        
    def return_keys(self):
        return self.graph_keys
        
    def return_num_nodes(self):
        return self.num_nodes
        
    def return_edge_prob(self):
        return self.probability
        
    def get_graph(self):
       return self.graph_dict

    def get_edges(self):
        return self.graph_dict.values()
        
       
    def create_edges(self):
        for item1 in self.graph_keys:
           for item2 in self.graph_keys:
               #print "Looking at :" , item1
               if item1 == item2:
                   pass

               else:
                   a = random.random()
                   if a < self.probability:
                       self.graph_dict[item1].add(item2)
                       
                       #print "1 Loop of generated edges complete"
        return self.graph_dict

#Helper Functions

def normalize(dict):
    total_nums = 0
    
    for item in dict.values():
        total_nums += item
        
    print "Total number of citations is :", total_nums
    
    dict_copy = {}
    
    for key in dict:
        dict_num = dict[key]
        dict_copy[key] = float(dict_num) / float(total_nums)
        #print dict_copy[key]
        
    return dict_copy

def remove_key(input_dict,key):
    
    if key not in input_dict.keys():
        return input_dict
    else:
        copy = dict(input_dict)
        del copy[key]
        return copy

#Initialize Code
test_class = AlgorithmER_directed(1000,0.75)
test_class.create_edges()


graph_dict_raw =  core_code.in_degree_distribution(test_class.get_graph())
graph_dict_norm = normalize(graph_dict_raw)
graph_dict = remove_key(graph_dict_norm,0)



plt.loglog(graph_dict.keys(), graph_dict.values(), 'ro')
plt.xscale('log')
plt.yscale('log')
plt.show()

        

#test_class = AlgorithmER_directed(6,0.5)

#print test_class.return_keys()
#print test_class.get_graph()
#test_class.create_edges()
#print test_class.get_graph()