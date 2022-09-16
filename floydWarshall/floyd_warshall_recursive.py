import sys

# random_graph = np.random.randint(9, size=(4, 4))
# graph = random_graph.tolist()
NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
# graph = [[0, 1, NO_PATH, NO_PATH],
#         [NO_PATH, 0, -1, NO_PATH],
#         [NO_PATH, NO_PATH, 0, -1],
#         [-1, NO_PATH, NO_PATH, 0]]
vertices = len(graph)

#vertices = (len(graph) + 1)
#vertices = vertice + 1
#print('Number of vertices:', vertices)

# Just testing GitHub again/ one more time
def shortestPath(i, j, k, p):
    if k < 0:
        return(p[i][j])
    elif i==j:
        return 0
    # elif k != vertices:
    #     raise IndexError('Number of vertices out of range. Check input')
    else:
        return min(shortestPath(i, j, k-1, p), shortestPath(i, k, k-1, p) + shortestPath(k, j, k-1, p))

def floydWarshall(dist_graph):
    for i in range(vertices):
        for j in range(vertices):
            try:
                dist_graph[i][j] = shortestPath(i, j, vertices -1 , dist_graph)
            except IndexError:
                it = iter(dist_graph)
                list_len = len(next(it))
                if not all(len(l) == list_len for l in it):
                    return print('graph shape has to be square')
                if vertices != len(dist_graph):
                    return print('Number of vertices out of range. Check input')
            except TypeError:
                if not any(isinstance(x, str) for x in dist_graph):
                    return print('graph contains an unsupported character type, ensure all characters are integers')
           
    printSolution(dist_graph)
    return dist_graph

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
    