import timeit
import sys
sys.path.insert(0, 'c:\\Users\\jason\\Documents\\Data Science and AI MSc\\Software Development in Practice\\mid_module_assessment\\floydWarshall')
# from floyd_warshall_recursive import *

NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
VERTICES = len(graph)

FLOYD_WARSHALL_1 = 'from floyd_warshall_recursive import floyd_warshall'
TEST_CODE_1 = '''
def floyd_warshall(dist_graph):
    for i in range(VERTICES):
        for j in range(VERTICES):
            try:
                dist_graph[i][j] = shortest_path(i, j, VERTICES - 1,
                                                 dist_graph)
            except IndexError:
                iterating_dist_graph = iter(dist_graph)
                list_len = len(next(iterating_dist_graph))
                if not all(len(list_in_graph) == list_len for list_in_graph
                           in iterating_dist_graph):
                    return print('raph shape has to be square')
                if VERTICES != len(dist_graph):
                    return print('Number of vertices out of range.\
 Check input')
            except TypeError:
                if not any(isinstance(x, str) for x in dist_graph):
                    return print('graph contains an unsupported character\
                                  type, ensure all characters are integers')

    print_solution(dist_graph)
    return dist_graph
'''

FLOYD_WARSHALL_2 = 'from floyd_warshall_recursive import shortest_path'
TEST_CODE_2 = '''
def shortest_path(i, j, k, distance_graph):
    if k < 0:
        return distance_graph[i][j]
    if i == j:
        return 0
    return min(shortest_path(i, j, k-1, distance_graph),
               shortest_path(i, k, k-1, distance_graph) +
               shortest_path(k, j, k-1, distance_graph))

'''
FLOYD_WARSHALL_3 = 'from floyd_warshall_recursive import print_solution'
TEST_CODE_3 = '''
def print_solution(dist_graph):
    print("Following matrix shows the shortest distances\
 between every pair of VERTICES")
    for i in range(VERTICES):
        for j in range(VERTICES):
            if dist_graph[i][j] == NO_PATH:
                print("%9s" % ("NO_PATH"), end="")
            else:
                print("%9d" % (dist_graph[i][j]), end='')
            if j == VERTICES-1:
                print()
'''

FLOYD_WARSHALL_4 = 'import floyd_warshall_recursive'
TEST_CODE_4 = '''
NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
# graph = [[0, 1, NO_PATH, NO_PATH],
#         [NO_PATH, 0, -1, NO_PATH],
#         [NO_PATH, NO_PATH, 0, -1],
#         [-1, NO_PATH, NO_PATH, 0]]
VERTICES = len(graph)

# VERTICES = (len(graph) + 1)
# VERTICES = vertice + 1
# print('Number of VERTICES:', VERTICES)

# Just testing GitHub again/ one more time


def shortest_path(i, j, k, distance_graph):
    if k < 0:
        return distance_graph[i][j]
    if i == j:
        return 0
    return min(shortest_path(i, j, k-1, distance_graph),
               shortest_path(i, k, k-1, distance_graph) +
               shortest_path(k, j, k-1, distance_graph))


def floyd_warshall(dist_graph):
    for i in range(VERTICES):
        for j in range(VERTICES):
            try:
                dist_graph[i][j] = shortest_path(i, j, VERTICES - 1,
                                                 dist_graph)
            except IndexError:
                iterating_dist_graph = iter(dist_graph)
                list_len = len(next(iterating_dist_graph))
                if not all(len(list_in_graph) == list_len for list_in_graph
                           in iterating_dist_graph):
                    return print('raph shape has to be square')
                if VERTICES != len(dist_graph):
                    return print('Number of vertices out of range.\
 Check input')
            except TypeError:
                if not any(isinstance(x, str) for x in dist_graph):
                    return print('graph contains an unsupported character\
                                  type, ensure all characters are integers')

    print_solution(dist_graph)
    return dist_graph
'''

FLOYD_WARSHALL_IMPERATIVE = 'import floyd_warshall_imperative'
TEST_CODE_IMPERATIVE = '''
NO_PATH = sys.maxsize

graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
VERTICES = len(graph[0])


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node\
        in itertools.product\
            (range(VERTICES), range(VERTICES), range(VERTICES)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate]
                                             + distance[intermediate][end_node]
                                             )

        # Any value that have sys.maxsize has no path
    print_solution(distance)
'''


print('The minimum value\'s from the timieit tests are:\n',
      'floyd_warshall function: ', min(timeit.repeat(
                                       stmt=TEST_CODE_1,
                                       setup=FLOYD_WARSHALL_1,
                                       number=1000)), 's\n',
      'shortestPath function: ', min(timeit.repeat(
                                     stmt=TEST_CODE_2,
                                     setup=FLOYD_WARSHALL_2,
                                     number=1000)), 's\n',
      'printSolution function: ', min(timeit.repeat(
                                      stmt=TEST_CODE_3,
                                      setup=FLOYD_WARSHALL_3,
                                      number=1000)), 's\n')

print(
      'Time comparison between the recursive and imperative applications of\
 the Floyd Warshall Algorithm: \n',
      'The floyd_warshall_recursive.py module: ',
      min(timeit.repeat(stmt=TEST_CODE_4,
                        setup=FLOYD_WARSHALL_4,
                        number=1000)), 's\n',
      'The floyd_warshall_imperative.py module: ',
      min(timeit.repeat(stmt=TEST_CODE_IMPERATIVE,
                        setup=FLOYD_WARSHALL_IMPERATIVE,
                        number=1000)), 's\n'
      )
