from linked_list import SinglyLinkedNode, SinglyLinkedList


def loop_length(l):
    loop_detected = False
    slow = l.head
    fast = l.head

    while not loop_detected:
        if (slow.child is None) or (fast.child is None) or (fast.child.child is None):
            return 0
        slow = slow.child
        fast = fast.child.child
        if slow is fast:
            loop_detected = True

    slow = slow.child
    fast = fast.child.child
    length = 1
    while slow is not fast:
        slow = slow.child
        fast = fast.child.child
        length += 1
    return length


def entry_point(l):
    n = loop_length(l)
    if n == 0:
        return None
    pilot = l.head
    laggard = l.head
    for _ in range(n):
        pilot = pilot.child

    while laggard is not pilot:
        laggard = laggard.child
        pilot = pilot.child
    return laggard



# TESTS
import unittest

class TestBase(unittest.TestCase):
    def create_list(self, length_neck, length_loop):
        neck = SinglyLinkedList()
        for i in range(length_neck):
            neck.prepend(SinglyLinkedNode(length_neck - i))

        loop = SinglyLinkedList()
        for i in range(length_loop):
            loop.prepend(SinglyLinkedNode(length_neck + length_loop - i))

        if loop.head is not None:
            end = loop.head
            while end.child is not None:
                end = end.child
            end.child = loop.head

            neck.append(loop.head)
        return neck


class loop_lengthTest(TestBase):
    def test_1(self):
        l = self.create_list(1, 5)
        self.assertEqual(loop_length(l), 5)

    def test_2(self):
        l = self.create_list(0, 100)
        self.assertEqual(loop_length(l), 100)

    def test_3(self):
        l = self.create_list(100,0)
        self.assertEqual(loop_length(l), 0)

    def test_4(self):
        l = self.create_list(15, 1)
        self.assertEqual(loop_length(l), 1)


class entry_pointTest(TestBase):
    def test_1(self):
        l = self.create_list(1, 5)
        self.assertEqual(entry_point(l).value, 2)

    def test_2(self):
        l = self.create_list(0, 100)
        self.assertEqual(entry_point(l).value, 1)

    def test_3(self):
        l = self.create_list(100, 0)
        self.assertIsNone(entry_point(l))

    def test_4(self):
        l = self.create_list(15, 1)
        self.assertEqual(entry_point(l).value, 16)