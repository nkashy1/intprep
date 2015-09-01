"""
In-place partition of singly-linked list. Runs in linear time.
"""

from linked_list import SinglyLinkedNode, SinglyLinkedList

def partition(linked_list, x):
    current_node = linked_list.head
    initial_candidate_parent = None
    while current_node.child is not None:
        if current_node.value >= x:
            if initial_candidate_parent is None:
                candidate = current_node.child
            else:
                candidate = initial_candidate_parent.child

            while candidate is not None:
                if candidate.value < x:
                    temp = current_node.value
                    current_node.value = candidate.value
                    candidate.value = temp
                    initial_candidate_parent = candidate
                    break
                candidate = candidate.child
            if candidate is None:
                return None
        current_node = current_node.child


# TESTS
import unittest

class partitionTests(unittest.TestCase):
    def test_1(self):
        linked_list = SinglyLinkedList()
        values = [3, 5, 8, 5, 10, 2, 1]
        for value in values:
            linked_list.append(SinglyLinkedNode(value))

        partition(linked_list, 5)

        traversal = linked_list.traverse()
        self.assertEqual(set(traversal[:3]), set([1,2,3]))
        self.assertEqual(set(traversal[3:]), set([5, 8, 10]))
        self.assertEqual(len(traversal), 7)

    def test_2(self):
        linked_list = SinglyLinkedList()
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for value in values:
            linked_list.append(SinglyLinkedNode(value))

        partition(linked_list, 10)

        traversal = linked_list.traverse()
        self.assertEqual(traversal, [9, 8, 7, 6, 5, 4, 3, 2, 1, 10])
