import unittest
import sys
from floyd_warshall_recursive import floydWarshall
from floyd_warshall_recursive import shortestPath
import numpy as np
#from floyd_warshall_recursive import printSolution

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

# vertices = 5 
#vertices = vertice + 1
# vertices = len(graph[0])

class testFloydWarshall(unittest.TestCase):
    def test_floydWarshall(self):
        NO_PATH = sys.maxsize
        test_graph = [[0, 7, NO_PATH, 8],
                    [NO_PATH, 0, 5, NO_PATH],
                    [NO_PATH, NO_PATH, 0, 2],
                    [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = floydWarshall(test_graph)
        expected = [[0, 7, 12, 8],
                    [NO_PATH, 0, 5, 7], 
                    [NO_PATH, NO_PATH, 0, 2], 
                    [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(actual, expected)

    def test_floydWarshall_incorrect_input(self):
        NO_PATH = sys.maxsize
        test_graph = [[0, 'x', NO_PATH, 'y'],
                    [NO_PATH, 0, 5, NO_PATH],
                    [NO_PATH, NO_PATH, 'z', 2],
                    [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = floydWarshall(test_graph)
        expected = print('graph contains an unsupported character type, ensure all characters are integers')
        self.assertEqual(actual, expected)

    # def test_floydWarshall_negative_loop(self):
    #     NO_PATH = sys.maxsize
    #     test_graph = [[0, -7, NO_PATH, 8],
    #                 [NO_PATH, 0, 5, NO_PATH],
    #                 [NO_PATH, NO_PATH, 0, 2],
    #                 [NO_PATH, NO_PATH, NO_PATH, 0]]
    #     actual = floydWarshall(test_graph)
    #     expected = print('A negative loop has been found')
    #     self.assertEqual(actual, expected)
    
    def test_floydWarshall_incorrect_graph_shape(self):
        NO_PATH = sys.maxsize
        test_graph = [0, 7, NO_PATH, 8]
        actual = floydWarshall(test_graph)
        expected = print('graph shape has to be square')
        self.assertEqual(actual, expected)

    def test_floydWarshall_different_graphs(self):
        NO_PATH = sys.maxsize
        graph_2 = [[0, 3, NO_PATH, 9], 
                    [3, 0, 7, 4],
                    [4, 7, 0, 1],
                    [NO_PATH, 2, 5, 0]]
        graph_3 = [[0, 5, 9, NO_PATH], 
                    [NO_PATH, 0, 5, 2],
                    [NO_PATH, NO_PATH, 0, 2],
                    [3, 1, 9, 0]]
        graph_4 = [[0, 7, NO_PATH],
                    [1, 0, NO_PATH],
                    [3, NO_PATH, 0]]
        graphs = [graph_2, graph_3, graph_4]
        
        for i in graphs:
            floydWarshall(i)

    # def test_floydWarshall_error(self):
    #     vertices = vertices + 1
    #     for i in range(vertices):
    #         for j in range(vertices):
    #             graph[i][j] = shortestPath(i, j, vertices, graph)
        
        actual = floydWarshall(graph)
        expected = print('Number of vertices out of range. Check input')
        self.assertEqual(actual, expected)

               
        

class testshortestPath(unittest.TestCase):
    def test_shortestPath_iequalsj(self):
    
        actual = shortestPath(1, 1, 3, graph)
        expected = 0
        self.assertEqual(actual, expected)

    def test_shortestPath_specific_graph_location(self):
        actual = shortestPath(1, 2, 3, graph)
        print(actual)
        expected = 5
        self.assertEqual(actual, expected)

    #def test_shortestPath_


    
        








                

# floydWarshall(graph)
