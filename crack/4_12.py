from MyStack import MyStack
from graphs import BinaryTreeVertex


def paths_with_sum(n, root):
    num_paths = 0

    itinerary = MyStack()
    itinerary.push((root, []))

    while not itinerary.isEmpty():
        v, old_sums = itinerary.pop()
        new_sums = [v.value]

        if v.value == n:
            num_paths += 1

        for s in old_sums:
            t = s + v.value
            if t == n:
                num_paths += 1
            new_sums.append(t)

        if v.right is not None:
            itinerary.push((v.right, new_sums))
        if v.left is not None:
            itinerary.push((v.left, new_sums))

    return num_paths



# TESTS
import unittest

class paths_with_sumTests(unittest.TestCase):
    def test_1(self):
        l = BinaryTreeVertex(2)
        r = BinaryTreeVertex(3)
        root = BinaryTreeVertex(1, l, r)

        result = paths_with_sum(3, root)
        self.assertEqual(result, 2)

    def test_2(self):
        ll = BinaryTreeVertex(3)
        lr = BinaryTreeVertex(4)
        l = BinaryTreeVertex(2, ll, lr)

        rl = BinaryTreeVertex(6)
        rr = BinaryTreeVertex(7)
        r = BinaryTreeVertex(5, rl, rr)

        root = BinaryTreeVertex(1, l, r)

        result = paths_with_sum(6, root)
        expected_result = 4
        self.assertEqual(result, expected_result)