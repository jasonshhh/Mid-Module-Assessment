import sys


# random_graph = np.random.randint(9, size=(4, 4))
# graph = random_graph.tolist()
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
    '''
    Finds the shortest path matrix in the input graph
    '''
    if k == 0:
        return distance_graph[i][j]
    if (i, j) != 0:
        return print('Check Input! There are numbers in the diagonals')
    return min(shortest_path(i, j, k - 1, distance_graph),
               shortest_path(i, k, k - 1, distance_graph) +
               shortest_path(k, j, k - 1, distance_graph))


def floyd_warshall(dist_graph):
    '''
    Reads the input graph and iterates through i and j,
    giving the values to shortest_path function
    '''
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
                    return print('graph shape has to be square')
                if VERTICES != len(dist_graph):
                    return print('Number of vertices out of range.\
 Check input')
            except TypeError:
                if i == j != 0:
                    return print('Check Input! There are numbers when i == j')
                if not any(isinstance(x, str) for x in dist_graph):
                    return print('graph contains an unsupported character\
type, ensure all characters are integers')
   
    print_solution(dist_graph)
    return dist_graph


# A utility function to print the solution
def print_solution(dist_graph):
    '''
    A utility function to print the solution
    '''
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


if __name__ == '__main__':
    floyd_warshall(graph)
