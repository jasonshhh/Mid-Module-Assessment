import timeit
import sys
sys.path.insert(0, 'c:\\Users\\jason\\Documents\\Data Science and AI MSc\\Software Development in Practice\\mid_module_assessment')
#from floyd_warshall_recursive import *

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
vertices = len(graph)

import_module1 = 'from floyd_warshall_recursive import floydWarshall'
testcode1 = ''' 
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
'''

import_module2 = 'from floyd_warshall_recursive import shortestPath'
testcode2 = '''
def shortestPath(i, j, k, p):
    if k < 0:
        return(p[i][j])
    elif i==j:
        return 0
    else:
        return min(shortestPath(i, j, k-1, p), shortestPath(i, k, k-1, p) + shortestPath(k, j, k-1, p))
'''
import_module3 = 'from floyd_warshall_recursive import printSolution'
testcode3 = '''
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
'''

import_module4 = 'import floyd_warshall_recursive'
testcode4 = '''
NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]
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
           

    return dist_graph


'''
import_module5 = 'import floyd_warshall_imperative'
testcode5 = '''
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
    print(distance)
'''


print('The minimum value\'s from the timieit tests are:\n',
'floydWarshall function: ', min(timeit.repeat(stmt=testcode1, setup=import_module1, number = 1000)),'s\n',
'shortestPath function: ', min(timeit.repeat(stmt=testcode2, setup=import_module2, number = 1000)),'s\n',
'printSolution function: ', min(timeit.repeat(stmt=testcode3, setup=import_module3, number = 1000)),'s\n')

print('Time comparison between the recursive and imperative applications of the Floyd Warshall Algorithm: \n',
'The floyd_warshall_recursive.py module: ', min(timeit.repeat(stmt=testcode4, setup=import_module4, number = 1000)),'s\n',
'The floyd_warshall_imperative.py module: ', min(timeit.repeat(stmt=testcode5, setup=import_module5, number = 1000)),'s\n'
)