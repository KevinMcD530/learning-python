# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:31:52 2016

A project to implement BFS an analyze node graphs.
returns sets of all nodes visisted during BFS while searching
through graph'''

#Algorithmic Thinking - Project 2 - BFS
#By: Kevin McDonald


"""



#import needed modules
import queue_class as poc_queue

import random
#import copy


#Example graphs for testing

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

EX_GRAPH3 = { 0 : set([1,2]),
            1 : set([0,2]),
            2 : set([0,1]),
            3 : set([4,5,6]),
            4 : set([3,5,6]),
            5 : set([3,4,6]),
            6 : set([3,4,5])}



def bfs_visited(ugraph, start_node):
    '''An implementation of BFS that takes an undirected 
    graph and a starting node and returns a set consisting
    of all nodes that are visited by the BFS'''
    
    #initialize empty queue to track visited nodes
    graph_queue = poc_queue.Queue()
    
    #set starting node and enqueue it
    visited = set([])
    visited.add(start_node)
    graph_queue.enqueue(start_node)
    #print "the queue now contains :",graph_queue.__str__()
    
    
    #Begin BFS
    while graph_queue.__len__() != 0:
        
        #take first item from queue, check its neighbors
        node_to_check = graph_queue.dequeue()
            
        for neighbor in ugraph[node_to_check]:
            if neighbor not in visited:
                visited.add(neighbor)
                graph_queue.enqueue(neighbor)
                #print "Queue updated, now contains :", graph_queue.__str__()
    
    return visited


def cc_visited(ugraph):
    '''function to return a list of sets of all the node connections
    in the entire graph. Runs bfs_visisted on each node and adds the resulting
    set to a list as the output'''
    
    #initialize connected components list and empty result lkist
    remaining_nodes = set(ugraph.keys())
    #remaining_nodes = poc_queue.Queue()
    
    #for item in remaining_nodes_raw:
        #remaining_nodes.enqueue(item)
        
    connected = []
    
    #main function loop
    while len(remaining_nodes) != 0:
        node_to_bfs = random.choice(tuple(remaining_nodes))
        bfs_set = bfs_visited(ugraph,node_to_bfs)
        #print bfs_set
        connected.append(bfs_set)
        
        for item in bfs_set:
            #print item
            remaining_nodes.remove(item)
        
    
    return connected


def largest_cc_size(ugraph):
    '''Takes a undirected graph input and returns the length of the
    largest connection portion of the graph'''
    
    max_num = 0
    
    cc_visited_output = cc_visited(ugraph)
    
    for item in cc_visited_output:
        if len(item) > max_num:
            max_num = len(item)
        else:
            pass
        
    return max_num
            

def compute_resilience(ugraph, attack_order):
    '''Function that systematically removes a node and its edges from the 
    original graph, and then computes the largets connected network following
    each removal. Returns a list that is the largest connected network at each
    step'''
    
    #initilize result list and add initial graph connection size to it
    result = largest_cc_size(ugraph)
    result_list = []
    result_list.append(result)
    
    
    for item in attack_order:
        #print ugraph
        ugraph.pop(item)
        
        #iterate over remaining nodes and take out "attacked" node
        for nodes in ugraph:
            ugraph[nodes].discard(item)
            
        iter_result = largest_cc_size(ugraph)
        result_list.append(iter_result)
    
    return result_list
    
print compute_resilience(EX_GRAPH3,[0,1,2])
                
        
        
    
    

    
