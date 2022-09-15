import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
vertices = len(graph[0])

def floyd(distance):
# """
# A simple implementation of Floyd's algorithm
# """
    for intermediate, start_node,end_node\
        in itertools.product\
            (range(vertices),range(vertices), range(vertices)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        #return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node] )
        #Any value that have sys.maxsize has no path
    printSolution(distance)

# A utility function to print the solution
def printSolution(graph):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(vertices):
        for j in range(vertices):
            if(graph[i][j] == NO_PATH):
                print("%9s" % ("NO_PATH"), end="")
            else:
                print("%9d" % (graph[i][j]), end='')
            if j == vertices-1:
                print()

# floyd(graph)