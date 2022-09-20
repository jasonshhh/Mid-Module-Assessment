import sys
import itertools

NO_PATH = sys.maxsize

graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
VERTICES = len(graph)


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node\
        in itertools.product(range(VERTICES),
                             range(VERTICES),
                             range(VERTICES)):
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


# A utility function to print the solution
def print_solution(distance):
    '''
    Prints the output in a more aesthetic format
    '''
    print("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(VERTICES):
        for j in range(VERTICES):
            if graph[i][j] == NO_PATH:
                print("%9s" % ("NO_PATH"), end='')
            else:
                print("%9d" % (distance[i][j]), end='')
            if j == VERTICES-1:
                print()


if __name__ == '__main__':
    floyd(graph)
