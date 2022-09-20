import timeit
import sys
import pandas as pd
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

    #print_solution(dist_graph)
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
    print("Below is the solution matrix with all pairs shortest paths:")
    for i in range(VERTICES):
        for j in range(VERTICES):
            if dist_graph[i][j] == NO_PATH:
                print("%9s" % ("NO_PATH"), end="")
            else:
                print("%9d" % (dist_graph[i][j]), end='')
            if j == VERTICES-1:
                print()
'''

FLOYD_WARSHALL_RECURSIVE = 'import floyd_warshall_recursive'
RECURSIVE_TEST_CODE = '''
NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
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

    return dist_graph
if __name__ == '__main__':
    floyd_warshall(graph)
'''

FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS = 'import \
                            floyd_warshall_imperative_itertools'
IMPERATIVE_ITERTOOLS_TESTCODE = '''
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
    #print_solution(distance)
if __name__ == '__main__':
    floyd(graph)
'''

FLOYD_WARSHALL_NESTED_RECURSIVE = 'import floyd_warshall_nested_recursive'
NESTED_RECURSIVE_TESTCODE = '''
NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
VERTICES = len(graph)
def floyd_warshall(dist_graph):
    def shortest_path(i, j, k):
        if k == 0:
            return dist_graph[i][j]
        if i == j:
            return 0
        # if i == j != 0:
        #     return print('Check Input! There are numbers in the diagonals')
        return min(shortest_path(i, j, k - 1),
                shortest_path(i, k, k - 1) +
                shortest_path(k, j, k - 1))

    for i in range(VERTICES):
        for j in range(VERTICES):
            try:
                dist_graph[i][j] = shortest_path(i, j, VERTICES - 1)
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

                if not any(isinstance(x, str) for x in dist_graph):
                    return print('graph contains an unsupported character\
type, ensure all characters are integers')
   
    #print_solution(dist_graph)
    return dist_graph

if __name__ == '__main__':
    floyd_warshall(graph)
'''

FLOYD_WARSHALL_IMPERATIVE = 'import floyd_warshall_imperative'
IMPERATIVE_TESTCODE = '''
NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
V = len(graph)

def floydWarshall(dist):
 
    for k in range(V):
 
        # pick all vertices as source one by one
        for i in range(V):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    #printSolution(dist)
    return(dist)


    # Driver's code
if __name__ == "__main__":

  # Function call
    floydWarshall(graph)
'''

FLOYD_WARSHALL_RECURSIVE_ITERTOOLS = 'import\
                 floyd_warshall_recursive_itertools'
RECURSIVE_ITERTOOLS_TEST_CODE = '''
import sys
import itertools

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

    if k == 0:
        return distance_graph[i][j]
    if i == j:
        return 0
    # if i == j != 0:
    #     return print('Check Input! There are numbers in the diagonals')
    return min(shortest_path(i, j, k - 1, distance_graph),
               shortest_path(i, k, k - 1, distance_graph) +
               shortest_path(k, j, k - 1, distance_graph))


def floyd_warshall(dist_graph):
    for i, j in itertools.product(range(VERTICES),
                                  range(VERTICES)):
        if i == j and shortest_path(i, j, VERTICES - 1,
                                    dist_graph) < 0:
            raise Exception('The solution contains negative loops')
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

            if not any(isinstance(x, str) for x in dist_graph):
                return print('graph contains an unsupported character\
type, ensure all characters are integers')

    #print_solution(dist_graph)
    return dist_graph

if __name__ == '__main__':
    floyd_warshall(graph)
'''

FLOYD_WARSHALL_NESTED_RECURSIVE_ITERTOOLS = 'import\
     floyd_warshall_nested_recursive_itertools'
NESTED_RECURSIVE_ITERTOOLS_TESTCODE = '''
import sys
import itertools

# random_graph = np.random.randint(9, size=(4, 4))
# graph = random_graph.tolist()
NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
VERTICES = len(graph)
# VERTICES = (len(graph) + 1)
# VERTICES = vertice + 1
# print('Number of VERTICES:', VERTICES)

# Just testing GitHub again/ one more time

def floyd_warshall(dist_graph):
    def shortest_path(i, j, k):

        if k == 0:
            return dist_graph[i][j]
        if i == j:
            return 0
        # if i == j != 0:
        #     return print('Check Input! There are numbers in the diagonals')
        return min(shortest_path(i, j, k - 1),
                shortest_path(i, k, k - 1) +
                shortest_path(k, j, k - 1))

    # for i in range(VERTICES):
    #     for j in range(VERTICES):
    for i, j in itertools.product(range(VERTICES),
                                  range(VERTICES)):
        try:
            dist_graph[i][j] = shortest_path(i, j, VERTICES - 1)
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
            if not any(isinstance(x, str) for x in dist_graph):
                return print('graph contains an unsupported character\
type, ensure all characters are integers')
   
    #print_solution(dist_graph)
    return dist_graph


if __name__ == '__main__':
    floyd_warshall(graph)
'''


# ---------------Phase 1 Analysis------------------

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

# ------------------Phase 2 Analysis-------------------

rec = min(timeit.repeat(stmt=RECURSIVE_TEST_CODE,
                        setup=FLOYD_WARSHALL_RECURSIVE,
                        number=1000))

imp = min(timeit.repeat(stmt=IMPERATIVE_ITERTOOLS_TESTCODE,
          setup=FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS,
          number=1000))

nest = min(timeit.repeat(stmt=NESTED_RECURSIVE_TESTCODE,
           setup=FLOYD_WARSHALL_NESTED_RECURSIVE,
           number=1000))

itera = min(timeit.repeat(stmt=IMPERATIVE_TESTCODE,
            setup=FLOYD_WARSHALL_IMPERATIVE,
            number=1000))


print(
      'Time comparison between the recursive and imperative applications of\
 the Floyd Warshall Algorithm: \n',
      'The floyd_warshall_recursive.py module: ', rec, 's\n',
      'The floyd_warshall_imperative.py module: ', imp, 's\n',
      'The nested function: ', nest, 's\n',
      'The iterative function', itera, 's'
      )

# --------------------Phase 3 Analysis-----------------------

imperative_faster = rec/imp
recursive_faster = imp/rec

if rec > imp:
    print('The imperative function is faster than the recursive by: ',
          rec - imp, 's\n',
          f'It is {imperative_faster} times faster than \
the recursive function.'
          )
if imp > rec:
    print('The recursive function is faster than the imperative\
 by: ',
          imp - rec, 's\n',
          f'It is {recursive_faster} times faster than the imperative function')


# --------------------Phase 4 Analysis-----------------------

def timeit_test_finding_imp_v_nested_rec_count(test_imp,
                                               fw_imp,
                                               tested_nest, 
                                               nested_func):
    '''
    Function for testing the time diff between
    nested recursive v imperative
    '''
    count = []
    for i in range(0, 1000):
        impe = timeit.timeit(stmt=test_imp,
                             setup=fw_imp, number=1)
        rece = timeit.timeit(stmt=tested_nest,
                             setup=nested_func, number=1)
        if impe < rece:
            count.append('imp')
        else:
            count.append('rec')
    imp_faster = count.count('imp')
    nest_faster = count.count('rec')
    print('------Comparison of Imperative and Nested Recursive------\n '
          'Runs: 1000\n',
          'Imperative Count: ', imp_faster, '\n',
          'Nested Recursive Count: ', nest_faster)


timeit_test_finding_imp_v_nested_rec_count(IMPERATIVE_ITERTOOLS_TESTCODE,
                                           FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS,
                                           NESTED_RECURSIVE_TESTCODE, 
                                           FLOYD_WARSHALL_NESTED_RECURSIVE)


def timeit_test_finding_iterative_v_nest_rec_count(test_iter,
                                                   fw_iter, 
                                                   tested_nest, 
                                                   nested_func):
    '''
    Function for testing the time diff between
    nested recursive and iterative
    '''
    count = []
    for i in range(0, 1000):
        ite = timeit.timeit(stmt=test_iter,
                            setup=fw_iter, number=1)
        rece = timeit.timeit(stmt=tested_nest,
                             setup=nested_func, number=1)
        if ite < rece:
            count.append('iter')
        else:
            count.append('rec')
    itera_faster = count.count('iter')
    nest_faster = count.count('rec')
    print('------Comparison of Iterative and Nested Recursive------\n '
          'Runs: 1000\n',
          'Iterative Count: ', itera_faster, '\n',
          'Nested Recursive Count: ', nest_faster)


timeit_test_finding_iterative_v_nest_rec_count(IMPERATIVE_TESTCODE, 
                                               FLOYD_WARSHALL_IMPERATIVE, 
                                               NESTED_RECURSIVE_TESTCODE, 
                                               FLOYD_WARSHALL_NESTED_RECURSIVE)


def timeit_test_finding_rec_v_nested_rec_count(tested_nest, 
                                               nested_func, 
                                               test_rec, 
                                               fw_func):
    '''
    Function for testing the time difference between
    the nested recursive and recursive functions
    '''
    count = []
    for i in range(0, 1000):
        nest_rec = timeit.timeit(stmt=tested_nest,
                                 setup=nested_func, number=1)
        rece = timeit.timeit(stmt=test_rec,
                             setup=fw_func, number=1)
        if nest_rec < rece:
            count.append('nest')
        else:
            count.append('rec')

    nest_faster = count.count('nest')
    rec_faster = count.count('rec')
    print('------Comparison of Nested Recursive and Recursive------\n '
          'Runs: 1000\n',
          'Recursive Count: ', rec_faster, '\n',
          'Nested Recursive Count: ', nest_faster)

timeit_test_finding_rec_v_nested_rec_count(NESTED_RECURSIVE_TESTCODE, 
                                           FLOYD_WARSHALL_NESTED_RECURSIVE, 
                                           RECURSIVE_TEST_CODE, 
                                           FLOYD_WARSHALL_RECURSIVE)


def timeit_test_finding_recursive_v_iterative_count(test_rec, 
                                                    fw_rec, 
                                                    test_iter, 
                                                    fw_iter):
    '''
    Function for testing the time difference between
    the recursive and iterative functions
    '''
    count = []
    for i in range(0, 1000):
        rece = timeit.timeit(stmt=test_rec,
                             setup=fw_rec, number=1)
        iter = timeit.timeit(stmt=test_iter,
                             setup=fw_iter, number=1)
        if iter < rece:
            count.append('iter')
        else:
            count.append('rec')

    iter_faster = count.count('iter')
    rec_faster = count.count('rec')
    print('------Comparison of Iterative and Recursive------\n '
          'Runs: 1000\n',
          'Recursive Count: ', rec_faster, '\n',
          'Iterative Count: ', iter_faster)

timeit_test_finding_recursive_v_iterative_count(RECURSIVE_TEST_CODE, 
                                                FLOYD_WARSHALL_RECURSIVE, 
                                                IMPERATIVE_TESTCODE, 
                                                FLOYD_WARSHALL_IMPERATIVE)


def timeit_test_finding_recursive_v_imperative_count(test_rec,
                                                     fw_rec,
                                                     test_imp,
                                                     fw_imp):
    '''
    Function for testing the time difference between
    the recursive and imperative functions
    '''
    count = []
    for i in range(0, 1000):
        rece = timeit.timeit(stmt=test_rec,
                             setup=fw_rec, number=1)
        impe = timeit.timeit(stmt=test_imp,
                             setup=fw_imp, number=1)
        if impe < rece:
            count.append('imp')
        else:
            count.append('rec')

    imp_faster = count.count('imp')
    rec_faster = count.count('rec')
    print('------Comparison of Recursive and Imperative------\n '
          'Runs: 1000\n',
          'Recursive Count: ', rec_faster, '\n',
          'Imperative Count: ', imp_faster)

timeit_test_finding_recursive_v_imperative_count(RECURSIVE_TEST_CODE, 
                                                 FLOYD_WARSHALL_RECURSIVE, 
                                                 IMPERATIVE_ITERTOOLS_TESTCODE, 
                                                 FLOYD_WARSHALL_IMPERATIVE)


def timeit_test_finding_iterative_v_imperative_count(test_iter, 
                                                     fw_iter, 
                                                     test_imp, 
                                                     fw_imp):
    '''
    Function for testing the time difference between
    the recursive and imperative functions
    '''
    count = []
    for i in range(0, 1000):
        ite = timeit.timeit(stmt=test_iter,
                            setup=fw_iter, number=1)
        impe = timeit.timeit(stmt=test_imp,
                             setup=fw_imp, number=1)
        if ite < impe:
            count.append('iter')
        else:
            count.append('impe')

    iter_faster = count.count('iter')
    impe_faster = count.count('impe')
    print('------Comparison of Iterative and Imperative------\n '
          'Runs: 1000\n',
          'Iterative Count: ', iter_faster, '\n',
          'Imperative Count: ', impe_faster)


#  ---------------------Phase 5 Analysis---------------------

# columns = ['recursive_count', 'recursive_itertools_count', 
#            'nested_recursive_count', 'nested_recursive_itertools_count',
#            'imperative_count', 'imperative_itertools_count']
df1 = pd.DataFrame()



recursive = min(timeit.repeat(stmt=RECURSIVE_TEST_CODE,
                              setup=FLOYD_WARSHALL_RECURSIVE,
                              number=1000))
recursive_itertools = min(timeit.repeat(stmt=RECURSIVE_ITERTOOLS_TEST_CODE,
                          setup=FLOYD_WARSHALL_RECURSIVE_ITERTOOLS,
                          number=1000))

nested_recursive = min(timeit.repeat(stmt=NESTED_RECURSIVE_TESTCODE,
                       setup=FLOYD_WARSHALL_NESTED_RECURSIVE,
                       number=1000))

nested_recursive_itertools = min(timeit.repeat(stmt=NESTED_RECURSIVE_ITERTOOLS_TESTCODE,
                                 setup=FLOYD_WARSHALL_NESTED_RECURSIVE_ITERTOOLS,
                                 number=1000))

imperative = min(timeit.repeat(stmt=IMPERATIVE_TESTCODE,
                 setup=FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS,
                 number=1000))

imperative_itertools = min(timeit.repeat(stmt=IMPERATIVE_ITERTOOLS_TESTCODE,
                           setup=FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS,
                           number=1000))

def finding_minimum_of_params(a, b, c, d, e, f, g, h, k, l, m, o, df1):
    '''
    This function is horrible to look at, was horrible to write
    and should probably be broken into a few more fucntions,
    but I'm outta time!
    It adds columns to the dataframe with values from all the 
    execution times
    '''
    execution_times = []
    count = []
    for num in range(0, 10000):
        execution_time = []

        recursive_ = timeit.timeit(stmt=a,
                                    setup=b,
                                number=1000)
        recursive_itertools_ = timeit.timeit(stmt=c,
                            setup=d,
                            number=1000)
        nested_recursive_ = timeit.timeit(stmt=e,
                        setup=f,
                        number=1000)
        nested_recursive_itertools_ = timeit.timeit(stmt=g,
                                    setup=h,
                                    number=1000)
        imperative_ = timeit.timeit(stmt=k,
                    setup=l,
                    number=1000)
        imperative_itertools_ = timeit.timeit(stmt=m,
                            setup=o,
                            number=1000)
            
        list_params = [recursive_, recursive_itertools_, nested_recursive_, nested_recursive_itertools_,
                        imperative_, imperative_itertools_]
            
        for i in list_params:
            execution_time.extend([i])
        execution_times.append(execution_time)
        
        # for q in list_params:
        #     
        #     if min_value:
        #         count.extend([1])
        #     else:
        #         count.extend([0])
        # counts.append()
        min_value = min(list_params)
        min_index = list_params.index(min_value)
        if min_index == 0:
            count.append('a')
        if min_index == 1:
            count.append('b')
        if min_index == 2:
            count.append('c')
        if min_index == 3:
            count.append('d')
        if min_index == 4:
            count.append('e')
        if min_index == 5:
            count.append('f')

        a_faster = count.count('a')
        b_faster = count.count('b')
        c_faster = count.count('c')
        d_faster = count.count('d')
        e_faster = count.count('e')
        f_faster = count.count('f')


    df1 = pd.DataFrame(execution_times, columns = ['recursive_execution_time', 'recursive_itertools_execution_time', 'nested_recursive_execution_time', 'nested_recursive_itertools_execution_time',
        'imperative_execution_time', 'imperative_itertools_execution_time'])

    new = df1[['recursive_execution_time', 'recursive_itertools_execution_time', 'nested_recursive_execution_time', 'nested_recursive_itertools_execution_time',
        'imperative_execution_time', 'imperative_itertools_execution_time']].idxmin(axis=1)
    
    new2 = df1[['recursive_execution_time', 'recursive_itertools_execution_time', 'nested_recursive_execution_time', 'nested_recursive_itertools_execution_time',
        'imperative_execution_time', 'imperative_itertools_execution_time']].min(axis=1)

    df1['fastest_version'] = new

    df1['fastest_version_time'] = new2

    print(df1)

    df1.to_csv(r'C:\Users\jason\Documents\Data Science and AI MSc\Software Development in Practice\mid_module_assessment\floydWarshall\expreiment.csv')

    print('------Comparison of all Parameters------\n '
        'Runs: 1000\n',
        'Recursive Count: ', a_faster, '\n',
        'Recursive Itertools Count: ', b_faster, '\n',
        'Nested Recursive Count : ', c_faster, '\n',
        'Nested Recursive Itertools Count : ', d_faster, '\n',
        'Imperative Count : ', e_faster, '\n',
        'Imperative Itertools Count: ', f_faster, '\n',
        )
    analysis(df1)
    return (df1)

def analysis(df1):
    '''
    Analysing various aspects of the dataframe 
    '''
    # count = df1['fastest_version'].count()
    # print(count)
    average_time_fastest = df1.groupby(['fastest_version']).mean()
    print('The versions that were the fastest and the average of their times : \n', average_time_fastest, '\n')
    df_average = df1[['recursive_execution_time', 'recursive_itertools_execution_time', 'nested_recursive_execution_time', 'nested_recursive_itertools_execution_time',
        'imperative_execution_time', 'imperative_itertools_execution_time']].mean(axis=0)
    print('Average times for all versions: \n', df_average, '\n')
    df_value_counts = df1['fastest_version'].value_counts()
    print('How many times a version was the fastest: \n', df_value_counts, '\n')
    df_fastest = [df_average.idxmin(), ':', df_average.min()]
    print('The fastest version overall : \n', df_fastest, '\n')



finding_minimum_of_params(RECURSIVE_TEST_CODE, FLOYD_WARSHALL_RECURSIVE,
                          RECURSIVE_ITERTOOLS_TEST_CODE, FLOYD_WARSHALL_RECURSIVE_ITERTOOLS,
                          NESTED_RECURSIVE_TESTCODE, FLOYD_WARSHALL_NESTED_RECURSIVE,
                          NESTED_RECURSIVE_ITERTOOLS_TESTCODE, FLOYD_WARSHALL_NESTED_RECURSIVE_ITERTOOLS,
                          IMPERATIVE_TESTCODE, FLOYD_WARSHALL_IMPERATIVE,
                          IMPERATIVE_ITERTOOLS_TESTCODE, FLOYD_WARSHALL_IMPERATIVE_ITERTOOLS, df1)


