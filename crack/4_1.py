from graphs import MathGraph

def exists_route(graph, source, destination):
    try:
        itinerary = graph.neighbors[source]
    except ValueError:
        raise

    visited = set([source])
    while len(itinerary) > 0:
        current = itinerary[0]
        if current == destination:
            return True
        elif current not in visited:
            for v in graph.neighbors[current]:
                itinerary.append(v)
        visited.add(current)
        itinerary = itinerary[1:]
    return False


# TESTS
import unittest

class exists_routeTests(unittest.TestCase):
    def test_1(self):
        V = [1, 2]
        E = [(1, 2)]
        G = MathGraph(V, E)

        self.assertTrue(exists_route(G, 1, 2))
        self.assertFalse(exists_route(G, 2, 1))
        self.assertFalse(exists_route(G, 1, 1))
        self.assertFalse(exists_route(G, 2, 2))

    def test_2(self):
        V = [1, 2, 3]
        E = [(1, 2), (2, 1), (3, 1)]
        G = MathGraph(V, E)

        self.assertTrue(exists_route(G, 1, 1))
        self.assertTrue(exists_route(G, 1, 2))
        self.assertTrue(exists_route(G, 2, 1))
        self.assertTrue(exists_route(G, 2, 2))
        self.assertTrue(exists_route(G, 3, 1))
        self.assertTrue(exists_route(G, 3, 2))
        self.assertFalse(exists_route(G, 1, 3))
        self.assertFalse(exists_route(G, 2, 3))
        self.assertFalse(exists_route(G, 3, 3))

    def test_3(self):
        V = [1, 2, 3, 4, 5, 6]
        E = [(1, 2), (2, 3), (3, 4), (4, 2), (4, 5)]
        G = MathGraph(V, E)

        self.assertFalse(exists_route(G, 1, 6))