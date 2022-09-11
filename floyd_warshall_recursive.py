import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
vertices = len(graph[0])
# Just testing GitHub
def shortestPath(i, j, k, p):
    if k < 0:
        return(p[i][j])
    elif i==j:
        return 0
    else:
        return min(shortestPath(i, j, k-1, p), shortestPath(i, k, k-1, p) + shortestPath(k, j, k-1, p))

def floydWarshall(dist_graph):
    for i in range(vertices):
        for j in range(vertices):
            dist_graph[i][j] = shortestPath(i, j, vertices - 1, dist_graph)
    printSolution(dist_graph)
    #return dist_graph

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
    
if __name__ == '__main__':
    floydWarshall(graph)
    