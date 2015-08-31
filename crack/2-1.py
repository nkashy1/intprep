from linked_list import SinglyLinkedNode, SinglyLinkedList

def deduplicate(linked_list):
    seen = set([])
    previous_node = None
    current_node = linked_list.head

    while current_node is not None:
        if current_node.value not in seen:
            seen.add(current_node.value)
            previous_node = current_node
            current_node = current_node.child
        else:
            previous_node.child = current_node.child
            current_node = current_node.child

# TEST
import unittest

class deduplicateTest(unittest.TestCase):
    def test_problem(self):
        linked_list = SinglyLinkedList(SinglyLinkedNode(-1))
        for i in range(100):
            linked_list.append(SinglyLinkedNode(i))
            linked_list.append(SinglyLinkedNode(i))

        for i in range(100):
            linked_list.append(SinglyLinkedNode(0))

        deduplicate(linked_list)
        self.assertEqual(linked_list.traverse(), [-1] + range(100))
