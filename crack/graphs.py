"""
Graph data structures for use in exercises involving graphs, trees, tries, etc.
"""

class MathGraph(object):
    def __init__(self, vertices, edges):
        """
        :param vertices: A set of vertex labels.
        :param edges: A set of pairs which represent directed edges from the first item to the second. The items should be vertex labels.
        :return: None
        """
        self.vertices = vertices
        self.neighbors = {v: [] for v in vertices}
        for e in edges:
            self.neighbors[e[0]].append(e[1])


class BinaryTreeVertex(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# TESTS
import unittest

class MathGraphTests(unittest.TestCase):
    def test_1(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (1, 3), (1, 4), (2, 1), (3, 1), (4, 1), (2, 3), (3, 4)]
        graph = MathGraph(vertices, edges)

        neighbors_1 = graph.neighbors[1]
        for j in range(3):
            self.assertIn(j+2, neighbors_1)

        neighbors_2 = graph.neighbors[2]
        expected = [1, 3]
        for j in expected:
            self.assertIn(j, neighbors_2)

        neighbors_3 = graph.neighbors[3]
        expected = [1, 4]
        for j in expected:
            self.assertIn(j, neighbors_3)

        self.assertIn(1, graph.neighbors[4])
