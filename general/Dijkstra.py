"""
Implementation of Dijkstra's algorithm to find the shortest route between two vertices in a graph.

This implementation makes use of the MathGraph data structure also defined here (but copied for the crack directory,
where there are tests for it).
"""

from Heap import BinaryHeap


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


def shortest_path(graph, v, w):
    assert v in graph.vertices
    assert w in graph.vertices

    path_data = {}
    for vertex in graph.vertices:
        if vertex == v:
            path_data[vertex] = {"name": vertex, "cost": 0, "predecessor": None}
        else:
            path_data[vertex] = {"name": vertex, "cost": float("inf"), "predecessor": None}

    def path_priority(x, y):
        if x["cost"] < y["cost"]:
            return -1
        elif x["cost"] == y["cost"]:
            return 0
        return 1

    remaining_vertices = BinaryHeap(priority=path_priority)
    for vertex in path_data:
        remaining_vertices.insert(path_data[vertex])

    while len(remaining_vertices) > 0:
        current = remaining_vertices.pop()
        neighbors = [vertex for vertex in graph.neighbors[current["name"]]]
        max_neighbor_cost = current["cost"] + 1
        for neighbor in neighbors:
            if path_data[neighbor]["cost"] > max_neighbor_cost:
                path_data[neighbor]["cost"] = max_neighbor_cost
                path_data[neighbor]["predecessor"] = current["name"]

    path = [w]
    while path_data[path[-1]]["predecessor"] is not None:
        path.append(path_data[path[-1]]["predecessor"])
    path.reverse()
    return path


# TESTS
import unittest

class DijkstraTests(unittest.TestCase):
    def test_1(self):
        graph = MathGraph([1, 2], [(1, 2)])
        result = shortest_path(graph, 1, 2)
        self.assertEqual(result, [1, 2])

    def test_2(self):
        graph = MathGraph([1], [])
        result = shortest_path(graph, 1, 1)
        self.assertEqual(result, [1])

    def test_3(self):
        graph = MathGraph([1, 2, 3, 4], [(1, 2), (2, 3), (1, 4), (3, 4)])

        result_1 = shortest_path(graph, 1, 2)
        self.assertEqual(result_1, [1, 2])

        result_2 = shortest_path(graph, 1, 4)
        self.assertEqual(result_2, [1, 4])

        result_3 = shortest_path(graph, 1, 3)
        self.assertEqual(result_3, [1, 2, 3])

    def test_4(self):
        graph = MathGraph([1, 2, 3, 4, 5, 6], [(1, 2), (1, 3), (2, 3), (3, 5), (5, 6), (2, 6)])
        result = shortest_path(graph, 1, 6)
        self.assertEqual(result, [1, 2, 6])
