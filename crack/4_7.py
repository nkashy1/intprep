import copy

from graphs import MathGraph


def build_order(graph):
    dependencies = {v: [] for v in graph.vertices}
    for v in graph.vertices:
        for w in graph.neighbors[v]:
            dependencies[w].append(v)

    unbuilt = copy.copy(graph.vertices)
    built = []

    while len(unbuilt) > 0:
        current = None
        for v in unbuilt:
            if dependencies[v] == []:
                current = v
                break

        if current is None:
            raise ValueError("Cycle detected in dependency graph.")

        for w in graph.neighbors[current]:
            dependencies[w].remove(current)

        built.append(current)
        unbuilt.remove(current)

    return built


# TESTS
import unittest

class build_orderTests(unittest.TestCase):
    def test_1(self):
        V = [1, 2, 3]
        E = [(1, 2), (1, 3), (2, 3)]
        graph = MathGraph(V, E)

        build = build_order(graph)
        self.assertEqual(build, [1, 2, 3])

    def test_2(self):
        V = [1, 2]
        E = [(1, 2), (2, 1)]
        graph = MathGraph(V, E)

        self.assertRaises(ValueError, build_order, graph)

    def test_3(self):
        V = ['a', 'b', 'c', 'd', 'f']
        E = [('f', 'a'), ('f', 'b'), ('a', 'd'), ('b', 'd'), ('d', 'c')]
        graph = MathGraph(V, E)

        build = build_order(graph)
        self.assertEqual(build, ['f', 'a', 'b', 'd', 'c'])

    def test_4(self):
        V = ['a', 'b', 'c', 'd', 'e', 'f']
        E = [('f', 'a'), ('f', 'b'), ('a', 'd'), ('b', 'd'), ('d', 'c')]
        graph = MathGraph(V, E)

        build = build_order(graph)
        self.assertEqual(build, ['e', 'f', 'a', 'b', 'd', 'c'])

    def test_5(self):
        V = ['a', 'b', 'c', 'd', 'e', 'f']
        E = [('f', 'a'), ('f', 'b'), ('a', 'd'), ('b', 'd'), ('d', 'c'), ('c', 'e'), ('e', 'a')]
        graph = MathGraph(V, E)

        self.assertRaises(ValueError, build_order, graph)
