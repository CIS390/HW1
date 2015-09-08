import Graph
import numpy as np

def straightLineDistance(g,a,b):
    """ Returns the distance between nodes a and b in Graph g """
    return np.linalg.norm(g.nodes[a]-g.nodes[b])

def astar(g,start,goal):
    """Implements the A-star algorithm with distance to the goal as a heuristic
    Input: g: Graph as specified in the Graph class, with N nodes, and edges for each node
           start: start node, a number from 0 to N-1
           goal: goal node, a number from 0 to N-1 (not necessarily distict from start)
    Output: a tuple (path, numopened)
            path: list of the indices of the nodes on the shortest path found
                starting with "start" and ending with "end"
            numopened: number of nodes opened while searching for the shortest path"""
    # Your code here
    return (list([]), 0)

def dijkstras(g,start,goal):
    """Implements Dijkstra's shortest path algorithm
    Input: g: Graph as specified in the Graph class, with N nodes, and edges for each node
           start: start node, a number from 0 to N-1
           goal: goal node, a number from 0 to N-1 (not necessarily distict from start)
    Output: a tuple (path, numopened)
            path: list of the indices of the nodes on the shortest path found
                starting with "start" and ending with "end"
            numopened: number of nodes opened while searching for the shortest path"""
    # Your code here
    return (list([]), 0)

