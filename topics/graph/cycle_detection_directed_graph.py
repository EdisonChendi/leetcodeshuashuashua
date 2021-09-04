import unittest
from typing import List
from pprint import pprint

# For directed Graph

# https://trykv.medium.com/algorithms-on-graphs-directed-graphs-and-cycle-detection-3982dfbd11f5
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/


class DirectedGraphCycleDetection:

    def solve(self, graph):
        def detect(node, visited, exploring):
            if node in visited:
                return False

            if node in exploring:
                return True

            exploring.add(node)

            for child in graph[node]:
                if detect(child, visited, exploring):
                    return True

            exploring.remove(node)
            visited.add(node)
            return False

        visited = set()
        for node in graph:
            if detect(node, visited, set()):
                return True
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B', 'C'},
            'B': {'C'},
            'C': {'D'},
            'D': {'E'},
            'E': {'B'}
        }
        expected = True
        self.assertEqual(algo.solve(graph), expected)

    def test_case_2(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B'},
            'B': {'C'},
            'C': {'E'},
            'D': {'A', 'B', 'F'},
            'E': {'D'},
            'F': {'B'}
        }
        expected = True
        self.assertEqual(algo.solve(graph), expected)

    def test_case_3(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D'},
            'D': set()
        }
        expected = False
        self.assertEqual(algo.solve(graph), expected)

    def test_case_4(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'A'},
        }
        expected = True
        self.assertEqual(algo.solve(graph), expected)

    def test_case_5(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B'},
            'B': {'A'}
        }
        expected = True
        self.assertEqual(algo.solve(graph), expected)

    def test_case_6(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B'},
            'C': {'B'},
            'B': set(),
        }
        expected = False
        self.assertEqual(algo.solve(graph), expected)

    def test_case_7(self):
        algo = DirectedGraphCycleDetection()
        graph = {
            'A': {'B'},
            'B': {'C'},
            'C': set(),
            'E': {'F'},
            'F': {'G', 'B'},
            'G': set(),
        }
        expected = False
        self.assertEqual(algo.solve(graph), expected)

    # def test_edge_case_1(self):
    #     sol = Solution()


if __name__ == "__main__":
    unittest.main()
