from linked_list import SinglyLinkedNode, SinglyLinkedList

def sumLists(a, b):
    current_a = a.head
    current_b = b.head
    result = SinglyLinkedList()

    # Digit addition step
    while (current_a is not None) and (current_b is not None):
        result.append(SinglyLinkedNode(current_a.value + current_b.value))
        current_a = current_a.child
        current_b = current_b.child
    while current_a is not None:
        result.append(SinglyLinkedNode(current_a.value))
        current_a = current_a.child
    while current_b is not None:
        result.append(SinglyLinkedNode(current_b.value))
        current_b = current_b.child

    # Carries step
    current_result = result.head
    while current_result is not None:
        if current_result.value >= 10:
            carry = int(current_result.value/10)
            current_result.value = current_result.value - 10*carry
            if current_result.child is not None:
                current_result.child.value += carry
            else:
                current_result.child = SinglyLinkedNode(carry)

        current_result = current_result.child

    return result



# TESTS
import unittest

class sumListsTests(unittest.TestCase):
    def list_rep(self, a_string):
        a = SinglyLinkedList()
        for digit in a_string:
            a.prepend(SinglyLinkedNode(int(digit)))
        return a

    def test_1(self):
        m = 617
        n = 295

        a = self.list_rep(str(m))
        b = self.list_rep(str(n))
        c = self.list_rep(str(m+n))

        result = sumLists(a, b)

        result_traversal = result.traverse()
        c_traversal = c.traverse()
        self.assertEqual(result_traversal, c_traversal)

    def test_2(self):
        m = 9999
        n = 99

        a = self.list_rep(str(m))
        b = self.list_rep(str(n))
        c = self.list_rep(str(m+n))

        result = sumLists(a, b)

        result_traversal = result.traverse()
        c_traversal = c.traverse()
        self.assertEqual(result_traversal, c_traversal)