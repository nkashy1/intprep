from linked_list import SinglyLinkedNode, SinglyLinkedList


def intersection_info(l1, l2):
    l1_iter = l1.head
    l1_length = 1
    while l1_iter.child is not None:
        l1_iter = l1_iter.child
        l1_length += 1

    l2_iter = l2.head
    l2_length = 1
    while l2_iter.child is not None:
        l2_iter = l2_iter.child
        l2_length += 1

    return (l1_iter is l2_iter, l1_length, l2_length)


def intersection(l1, l2):
    hook, length1, length2 = intersection_info(l1, l2)
    if hook is False:
        return None

    l1_iter = l1.head
    l2_iter = l2.head
    if length1 > length2:
        counter = length1 - length2
        while counter > 0:
            l1_iter = l1_iter.child
            counter -= 1
    elif length2 > length1:
        counter = length2 - length1
        while counter > 0:
            l2_iter = l2_iter.child
            counter -= 1

    while l1_iter.child is not None:
        if l1_iter is l2_iter:
            return l1_iter
        l1_iter = l1_iter.child
        l2_iter = l2_iter.child

    return l1_iter


# TESTS
import unittest


class TestBase(unittest.TestCase):
    def build_list(self, values):
        l = SinglyLinkedList()
        for value in values[::-1]:
            l.prepend(SinglyLinkedNode(value))
        return l


class intersection_infoTests(TestBase):
    def test_1(self):
        common = SinglyLinkedNode(0)
        l1 = SinglyLinkedList(common)
        l2 = SinglyLinkedList(common)

        self.assertEqual(intersection_info(l1, l2), (True, 1, 1))

    def test_2(self):
        l1 = SinglyLinkedList(SinglyLinkedNode(1))
        l2 = SinglyLinkedList(SinglyLinkedNode(2))

        self.assertEqual(intersection_info(l1, l2), (False, 1, 1))

    def test_3(self):
        common_values = ['common']*30
        common = self.build_list(common_values)

        l1_front_values = range(100)
        l1 = self.build_list(l1_front_values)
        l1.append(common.head)

        l2_front_values = range(10)
        l2 = self.build_list(l2_front_values)
        l2.append(common.head)

        self.assertEqual(intersection_info(l1, l2), (True, 130, 40))


class intersectionTests(TestBase):
    def test_1(self):
        common = SinglyLinkedNode(0)
        l1 = SinglyLinkedList(common)
        l2 = SinglyLinkedList(common)

        self.assertIs(intersection(l1, l2), common)

    def test_2(self):
        l1 = SinglyLinkedList(SinglyLinkedNode(1))
        l2 = SinglyLinkedList(SinglyLinkedNode(2))

        self.assertIsNone(intersection(l1, l2))

    def test_3(self):
        common_values = ['common']*30
        common = self.build_list(common_values)

        l1_front_values = range(100)
        l1 = self.build_list(l1_front_values)
        l1.append(common.head)

        l2_front_values = range(10)
        l2 = self.build_list(l2_front_values)
        l2.append(common.head)

        self.assertIs(intersection(l1, l2), common.head)