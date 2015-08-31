from linked_list import SinglyLinkedNode, SinglyLinkedList

def deleteFromMiddle(node):
    if node.child is None:
        raise ValueError("wtf")

    current_node = node
    while current_node.child.child is not None:
        current_node.value = current_node.child.value
        current_node = current_node.child

    current_node.value = current_node.child.value
    current_node.child = None



# TESTS
import unittest

class deleteFromMiddleTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList(SinglyLinkedNode(0))
        for i in range(3):
            self.linked_list.append(SinglyLinkedNode(i+1))

    def test_1(self):
        node = self.linked_list.head.child
        deleteFromMiddle(node)

        traversal = self.linked_list.traverse()
        self.assertEqual(len(traversal), 3)
        self.assertEqual(traversal, [0, 2, 3])

    def test_2(self):
        node = self.linked_list.head.child.child
        deleteFromMiddle(node)

        traversal = self.linked_list.traverse()
        self.assertEqual(len(traversal), 3)
        self.assertEqual(traversal, [0, 1, 3])

    def test_3(self):
        for _ in range(2):
            node = self.linked_list.head.child
            deleteFromMiddle(node)

        traversal = self.linked_list.traverse()
        self.assertEqual(len(traversal), 2)
        self.assertEqual(traversal, [0, 3])

    def test_4(self):
        node = self.linked_list.head.child.child.child
        self.assertRaises(ValueError, deleteFromMiddle, node)
