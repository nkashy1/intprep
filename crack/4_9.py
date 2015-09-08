import copy

from graphs import BinaryTreeVertex


def shuffles(a, b):
    la = len(a)
    lb = len(b)

    shuffles = [{"shuffle": [], "a": 0, "b": 0}]

    persist = True
    while persist:
        persist = False
        new_shuffles = []
        for x in shuffles:
            if x["a"] < la:
                y = copy.deepcopy(x)
                y["shuffle"].append(a[y["a"]])
                y["a"] = y["a"] + 1
                new_shuffles.append(y)
                persist = True
            if x["b"] < lb:
                y = copy.deepcopy(x)
                y["shuffle"].append(b[y["b"]])
                y["b"] = y["b"] + 1
                new_shuffles.append(y)
                persist = True

        if persist:
            shuffles = new_shuffles

    return {tuple(x["shuffle"]) for x in shuffles}


def possible_arrays(vertex):
    if vertex is None:
        return None
    l = possible_arrays(vertex.left)
    r = possible_arrays(vertex.right)

    if l is None and r is None:
        return {(vertex.value,)}
    elif l is None:
        return {tuple([vertex.value] + list(tail)) for tail in r}
    elif r is None:
        return {tuple([vertex.value] + list(tail)) for tail in l}

    tails = set([])
    for x in l:
        for y in r:
            s = shuffles(x, y)
            for tail in s:
                tails.add(tail)

    return {tuple([vertex.value] + list(tail)) for tail in tails}


# TESTS
import unittest

class shufflesTests(unittest.TestCase):
    def test_1(self):
        a = (1,)
        b = (2,)

        result = shuffles(a, b)
        expected = {(1, 2), (2, 1)}
        self.assertEqual(result, expected)

    def test_2(self):
        a = (1, 2)
        b = (3,)

        result = shuffles(a, b)
        expected = {(1, 2, 3), (1, 3, 2), (3, 1, 2)}
        self.assertEqual(result, expected)

    def test_3(self):
        a = (1, 2)
        b = (3, 4)

        result = shuffles(a, b)
        expected = {(1, 2, 3, 4), (1, 3, 2, 4), (3, 1, 2, 4), (1, 3, 4, 2), (3, 4, 1, 2), (3, 1, 4, 2)}
        self.assertEqual(result, expected)

    def test_4(self):
        a = (1, 2)
        b = (1,)

        result = shuffles(a, b)
        expected = {(1, 2, 1), (1, 1, 2)}
        self.assertEqual(result, expected)


class possible_arraysTests(unittest.TestCase):
    def test_1(self):
        l = BinaryTreeVertex(1)
        r = BinaryTreeVertex(3)
        root = BinaryTreeVertex(2, l,r)

        result = possible_arrays(root)
        expected = {(2, 1, 3), (2, 3, 1)}
        self.assertEqual(result, expected)

    def test_2(self):
        root = BinaryTreeVertex(1)

        result = possible_arrays(root)
        expected = {(1,)}
        self.assertEqual(result, expected)

    def test_3(self):
        ll = BinaryTreeVertex(4)
        l = BinaryTreeVertex(5, ll)
        rl = BinaryTreeVertex(11)
        r = BinaryTreeVertex(15, rl)
        root = BinaryTreeVertex(10, l, r)

        result = possible_arrays(root)
        expected = {(10, 5, 4, 15, 11), (10, 5, 15, 4, 11), (10, 15, 5, 4, 11),
                    (10, 5, 15, 11, 4), (10, 15, 5, 11, 4), (10, 15, 11, 5, 4)}
        self.assertEqual(result, expected)
