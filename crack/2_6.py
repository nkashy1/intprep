from linked_list import SinglyLinkedNode, SinglyLinkedList

def palindromic(l):
    r = SinglyLinkedList()

    current = l.head
    while current is not None:
        r.prepend(SinglyLinkedNode(current.value))
        current = current.child

    l_iter = l.head
    r_iter = r.head
    while l_iter is not None:
        if l_iter.value != r_iter.value:
            return False
        l_iter = l_iter.child
        r_iter = r_iter.child
    return True



# TESTS
import unittest

class palindromicTests(unittest.TestCase):
    def build_list_from_string(self, s):
        l = SinglyLinkedList()
        for c in s[::-1]:
            l.prepend(SinglyLinkedNode(c))
        return l

    def test_1(self):
        l = self.build_list_from_string('bob')
        self.assertTrue(palindromic(l))

    def test_2(self):
        l = self.build_list_from_string('alice')
        self.assertFalse(palindromic(l))

    def test_3(self):
        l = self.build_list_from_string('asdfasdffdsafdsa')
        self.assertTrue(palindromic(l))
