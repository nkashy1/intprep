"""
Linked list implementations for use in the exercises.
"""

class SinglyLinkedNode(object):
    def __init__(self, value, child=None):
        self.value = value
        self.child = child
    
    def link(self, child):
        self.child = child


class SinglyLinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self, node):
        current = self.head
        while current.child is not None:
            current = current.child
        current.child = node

    def traverse(self):
        current = self.head
        values = []
        while current is not None:
            values.append(current.value)
            current = current.child
        return values



# TESTS
import unittest

class SinglyLinkedNodeTest(unittest.TestCase):
    def setUp(self):
        self.child = SinglyLinkedNode(1)
        self.parent = SinglyLinkedNode(0, self.child)
        self.grandchild = SinglyLinkedNode(2)
    
    def test_constructor(self):
        self.assertIs(self.parent.child, self.child)
        self.assertIsNone(self.child.child)
        self.assertIsNone(self.grandchild.child)
        
        self.assertEqual(self.parent.value, 0)
        self.assertEqual(self.child.value, 1)
        self.assertEqual(self.grandchild.value, 2)
    
    def test_link(self):
        self.child.link(self.grandchild)
        self.assertIs(self.child.child, self.grandchild)


class SinglyLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.head = SinglyLinkedNode(0)
        self.linked_list = SinglyLinkedList(self.head)

    def test_constructor(self):
        self.assertIs(self.linked_list.head, self.head)

    def test_append(self):
        new_node = SinglyLinkedNode(1)
        self.linked_list.append(new_node)
        self.assertIs(self.linked_list.head.child, new_node)

        newer_node = SinglyLinkedNode(2)
        newest_node = SinglyLinkedNode(3)
        newer_node.link(newest_node)
        self.linked_list.append(newer_node)

        self.assertIs(new_node.child, newer_node)

        values = []
        current_node = self.linked_list.head
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.child

        self.assertEqual(values, [0, 1, 2, 3])

    def test_traverse(self):
        for i in range(100):
            self.linked_list.append(SinglyLinkedNode(i))
        self.assertEqual(self.linked_list.traverse(), [0] + range(100))
