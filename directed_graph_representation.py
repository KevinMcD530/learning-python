# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:07:16 2016

@author: kmcdonal
"""

#Representing Directed Graphs
#Kevin McDonald

'''A simple project where we represent graphs as dictionaries
assigned to variables'''

EX_GRAPH0 = { 0 : set([1,2]),
            1 : set([]),
            2 : set([])}


EX_GRAPH1 = { 0 : set([1,4,5]),
              1 : set([2,6]),
              2 : set([3]),
              3 : set([0]),
              4 : set([1]),
              5 : set([2]),
            6 : set([])}

EX_GRAPH2 = { 0 : set([1,4,5]),
              1: set([2,6]),
              2 : set([3,7]),
              3 : set([7]),
              4 : set([1]),
              5 : set([2]),
              7 : set([3]),
             6: set([]),
              8 : set([1,2]),
              9 : set([0,3,4,5,6,7]) }


def make_complete_graph(num_nodes):
    ''' a function to take a number of nodes and return a dictionary
    corresponding to a complete directed graph with that number 
    of nodes'''
    
    
    if num_nodes < 0:
        empty_dictionary = { }
        return empty_dictionary
    
    elif num_nodes == 1:
        solo_node = {0 : set([]) }
        return solo_node
    
    else:
        complete_graph = { }
        for num in range(num_nodes):
            temp_list = range(num_nodes)
            temp_list.remove(num)
            complete_graph[num] = set(temp_list)
            
        return complete_graph


    
    
def compute_in_degrees(digraph):
    '''Function to take a graph represented as a dictionary and returns 
    the in-node degree of each node - represented as a new dictionary''' 
    
    complete_in_graph =  { }
    values = []
    for key in digraph:
        values += list(digraph[key])
        complete_in_graph[key] = 0
    
    for value in values:
        complete_in_graph[value] += 1
    
    return complete_in_graph



def in_degree_distribution(digraph):
    '''
    Computes in-degree distribution for provided
    in-node dictionary
    '''
    
    final_result = {}
    
    in_degrees = compute_in_degrees(digraph).values()
    
    for degree in in_degrees:
        if degree in final_result:
            pass
        else:
            final_result[degree] = in_degrees.count(degree)
            
            
            
    return final_result
    


#print compute_in_degrees(EX_GRAPH2)
                             
    
    
    
    
    
    