#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:34:32 2018

@author: kefei
"""

def bfs(graph, start):
    """An algorithm that determine the shortest path from each vertex to every other vertex."""
    shortest_path = []
    prev_end_list = [start]
    prev_end = start
    
    for end in graph:  
        if start != end:  # set an end number that cannot be the same as start one
            queue = []
            queue.append([start])
            
            while queue:
                path = queue.pop(0)
                node = path[-1]
                if end in prev_end_list:  # check if the number we want to end is alreay did once before
                    pass
                else:
                    if node == end:  # find the shortest path
                        shortest_path.append(path)
                        prev_end = end
                        prev_end_list.append(prev_end)
                    
                    else:
                        for adjacent in graph.get(node, []):  # enumerate adjacent element
                            new_path = list(path)  # construct a new path
                            new_path.append(adjacent)  # push to the queue
                            queue.append(new_path)        
    print(shortest_path)


# Test out your solution to show it works as advertised. 
# Use textutal output, or, if you can, perhaps using a program like graphviz.
graph = {
    0: [],
    1: [3, 7],
    2: [1, 4, 8],
    3: [5],
    4: [],
    5: [],
    6: [],
    7: [6],
    8: [0, 9],
    9: []
}

bfs(graph, 2)
bfs(graph, 1)