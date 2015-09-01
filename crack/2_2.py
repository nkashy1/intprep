from linked_list import SinglyLinkedNode, SinglyLinkedList

def toLast(k, linked_list):
    assert k > 0
    pilot = linked_list.head
    laggard = None
    pilot_steps = 0
    while pilot_steps < k:
        pilot = pilot.child
        if pilot is None:
            return None
        pilot_steps += 1
    laggard = linked_list.head

    while pilot.child is not None:
        pilot = pilot.child
        laggard = laggard.child

    return laggard.value


# TESTS
import unittest

class toLastTests(unittest.TestCase):
    def test_1(self):
        linked_list = SinglyLinkedList(SinglyLinkedNode(0))
        for i in range(1, 100):
            linked_list.append(SinglyLinkedNode(i))

        self.assertEqual(toLast(1, linked_list), 98)

    def test_2(self):
        linked_list = SinglyLinkedList(SinglyLinkedNode(-1))
        for i in range(100):
            linked_list.append(SinglyLinkedNode(i))

        self.assertIsNone(toLast(1000, linked_list))

    def test_3(self):
        linked_list = SinglyLinkedList(SinglyLinkedNode(0))
        last = 100000
        current = last
        current_node = SinglyLinkedNode(current)
        while current > 0:
            current -= 1
            current_node = SinglyLinkedNode(current, current_node)
        linked_list.append(current_node)

        k = 7623

        self.assertEqual(toLast(k, linked_list), last - k)