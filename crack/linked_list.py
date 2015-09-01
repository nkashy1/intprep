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
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.child is not None:
                current = current.child
            current.child = node

    def prepend(self, node):
        if self.head is None:
            self.head = node
        else:
            tail_head = self.head
            self.head = node
            self.append(tail_head)

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


class SinglyLinkedListTests(unittest.TestCase):
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

    def test_prepend(self):
        new_head = SinglyLinkedNode(-1)
        new_head_child = SinglyLinkedNode(-2)
        new_head.link(new_head_child)

        self.linked_list.prepend(new_head)

        self.assertIs(self.linked_list.head, new_head)
        self.assertIs(self.linked_list.head.child, new_head_child)
        self.assertIs(self.linked_list.head.child.child, self.head)
        self.assertIsNone(self.linked_list.head.child.child.child)


class EmptySinglyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()

    def test_constructor(self):
        self.assertIsNone(self.linked_list.head)

    def test_append(self):
        node = SinglyLinkedNode(0)
        self.linked_list.append(node)
        self.assertIs(self.linked_list.head, node)

    def test_prepend(self):
        node = SinglyLinkedNode(0)
        self.linked_list.prepend(node)
        self.assertIs(self.linked_list.head, node)

    def test_traverse(self):
        traversal = self.linked_list.traverse()
        self.assertEqual(traversal, [])
