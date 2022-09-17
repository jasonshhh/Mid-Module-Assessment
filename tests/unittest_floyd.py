import unittest
import sys
sys.path.insert(0, 'c:\\Users\\jason\\Documents\\Data Science and AI MSc\\Software Development in Practice\\mid_module_assessment')
from floydWarshall.floyd_warshall_recursive import *
from floydWarshall.floyd_warshall_imperative import floyd



# from floydWarshall.floyd_warshall_recursive import floyd_warshall
# from floydWarshall.floyd_warshall_recursive import shortest_path

# from floyd_warshall_recursive import printSolution

NO_PATH = sys.maxsize
graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

VERTICES = len(graph)
# VERTICES = vertice + 1
# VERTICES = len(graph[0])


class TestFloydWarshall(unittest.TestCase):
    '''
    Class defining TestFloydWarshall
    '''
    def test_floyd_warshall(self):
        '''
        Tesitng the floyd_warshall function
        '''
        no_path = sys.maxsize
        test_graph = [
                     [0, 7, no_path, 8],
                     [no_path, 0, 5, no_path],
                     [no_path, no_path, 0, 2],
                     [no_path, no_path, no_path, 0]
                     ]
        actual = floyd_warshall(test_graph)
        expected = [
                   [0, 7, 12, 8],
                   [no_path, 0, 5, 7],
                   [no_path, no_path, 0, 2],
                   [no_path, no_path, no_path, 0]
                   ]
        self.assertEqual(actual, expected)

    def test_floyd_warshall_incorrect_input(self):
        '''
        Testing the function for incorrect input matrix
        '''
        no_path = sys.maxsize
        test_graph = [
                     [0, 'x', no_path, 'y'],
                     [no_path, 0, 5, no_path],
                     [no_path, no_path, 'z', 2],
                     [no_path, no_path, no_path, 0]
                     ]
        actual = floyd_warshall(test_graph)
        expected = print('graph contains an unsupported character type, \
ensure all characters are integers')
        self.assertEqual(actual, expected)


    # def test_floyd_warshall_negative_loop(self):
    #     no_path = sys.maxsize
    #     test_graph = [[0, -7, no_path, 8],
    #                 [no_path, 0, 5, no_path],
    #                 [no_path, no_path, 0, 2],
    #                 [no_path, no_path, no_path, 0]]
    #     actual = floydWarshall(test_graph)
    #     expected = print('A negative loop has been found')
    #     self.assertEqual(actual, expected)
    

    def test_floyd_warshall_incorrect_graph_shape(self):
        '''
        Tests for incorrect graph shape
        '''
        no_path = sys.maxsize
        test_graph = [0, 7, no_path, 8]
        actual = floyd_warshall(test_graph)
        expected = print('graph shape has to be square')
        self.assertEqual(actual, expected)

    def test_floyd_warshall_different_graphs(self):
        '''
        Tests the function with differecnt input graphs
        '''
        no_path = sys.maxsize
        graph_2 = [
                  [0, 3, no_path, 9],
                  [3, 0, 7, 4],
                  [4, 7, 0, 1],
                  [no_path, 2, 5, 0]
                  ]
        graph_3 = [
                  [0, 5, 9, no_path],
                  [no_path, 0, 5, 2],
                  [no_path, no_path, 0, 2],
                  [3, 1, 9, 0]
                  ]
        graph_4 = [
                  [0, 7, no_path],
                  [1, 0, no_path],
                  [3, no_path, 0]
                  ]
        graphs = [graph_2, graph_3, graph_4]

        for i in graphs:
            floyd_warshall(i)

    # def test_floydWarshall_error(self):
    #     vertices = vertices + 1
    #     for i in range(vertices):
    #         for j in range(vertices):
    # #             graph[i][j] = shortestPath(i, j, vertices, graph)
    #     actual = floydWarshall(graph)
    #     expected = print('Number of vertices out of range. Check input')
    #     self.assertEqual(actual, expected)


class TestShortestPath(unittest.TestCase):
    '''
    Tests shortest_path function
    '''
    def test_shortest_path_iequalsj(self):
        '''
        Tests if i == j
        '''
        no_path = sys.maxsize
        test_graph = [
                [0, 7, no_path, 8],
                [no_path, 0, 5, no_path],
                [no_path, no_path, 0, 2],
                [no_path, no_path, no_path, 0]
                ]
        actual = shortest_path(1, 1, 3, test_graph)
        expected = 0
        self.assertEqual(actual, expected)

    def test_shortest_path_specific_graph_location(self):
        '''
        Tests for a specific location in the input matrix
        '''
        no_path = sys.maxsize
        test_graph = [
                [0, 7, no_path, 8],
                [no_path, 0, 5, no_path],
                [no_path, no_path, 0, 2],
                [no_path, no_path, no_path, 0]
                ]
        actual = shortest_path(1, 2, 3, test_graph)
        print(actual)
        expected = 5
        self.assertEqual(actual, expected)


# floyd_warshall(graph)
