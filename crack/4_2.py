from graphs import BinaryTreeVertex

def lowest_bst(sorted_array):
    l = len(sorted_array)
    if l == 0:
        return None
    elif l == 1:
        return BinaryTreeVertex(sorted_array[0], None, None)
    else:
        mid = l/2
        return BinaryTreeVertex(sorted_array[mid], lowest_bst(sorted_array[:mid]), lowest_bst(sorted_array[mid+1:]))



# TESTS
import unittest

class lowest_bstTest(unittest.TestCase):
    def in_order_traversal(self, root):
        if root is None:
            return []
        else:
            return self.in_order_traversal(root.left) + [root.value] + self.in_order_traversal(root.right)

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def test_1(self):
        a = range(3)
        root = lowest_bst(a)
        self.assertEqual(self.in_order_traversal(root), a)
        self.assertEqual(self.height(root), 2)

    def test_2(self):
        a = range(63)
        root = lowest_bst(a)
        self.assertEqual(self.in_order_traversal(root), a)
        self.assertEqual(self.height(root), 6)

    def test_3(self):
        a = range(64)
        root = lowest_bst(a)
        self.assertEqual(self.in_order_traversal(root), a)
        self.assertEqual(self.height(root), 7)
