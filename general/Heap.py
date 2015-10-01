"""
Binary heap implementation.
"""

# ORDERINGS
def lt(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def gt(a, b):
    if a > b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

class BinaryHeap(object):
    def __init__(self, values=[], priority = lt):
        self.value_list = [value for value in values]
        self.priority = priority

    def __len__(self):
        return len(self.value_list)

    def pop(self):
        if len(self) == 0:
            return None

        result = self.value_list[0]
        self.delete(0)
        return result

    def insert(self, value):
        self.value_list.append(value)
        self.bubble_up(len(self)-1)

    def delete(self, index):
        assert index < len(self)

        last = self.value_list.pop()
        if index < len(self):
            self.value_list[index] = last
            self.bubble_up(index)
            self.bubble_down(index)

    def bubble_up(self, index):
        assert index < len(self)

        while True:
            if index == 0:
                break

            parent_index = (index - 1)/2

            if self.priority(self.value_list[index], self.value_list[parent_index]) <= 0:
                temp = self.value_list[parent_index]
                self.value_list[parent_index] = self.value_list[index]
                self.value_list[index] = temp
                index = parent_index
            else:
                break

    def bubble_down(self, index):
        assert index < len(self)

        while True:
            possible_child_indices = [2*index + 1, 2*index + 2]
            child_indices = [j for j in possible_child_indices if j < len(self)]
            indices_in_play = [index] + child_indices
            switchable_index = self.prioritize_indices(indices_in_play)[0]
            if switchable_index != index:
                temp = self.value_list[switchable_index]
                self.value_list[switchable_index] = self.value_list[index]
                self.value_list[index] = temp
                index = switchable_index
            else:
                break

    def prioritize_indices(self, indices):
        return sorted(indices, cmp=self.index_priority)

    def index_priority(self, i, j):
        return self.priority(self.value_list[i], self.value_list[j])


# TESTS
import unittest

class BinaryHeapTests(unittest.TestCase):
    def test_initialization(self):
        heap = BinaryHeap((1, 2, 3), gt)
        self.assertEqual(heap.value_list, [1, 2, 3])
        self.assertEqual(heap.priority(2, 1), -1)
        self.assertEqual(heap.priority(123, 123213213), 1)
        self.assertEqual(heap.priority(1,1), 0)

    def test_bubble_up_1(self):
        initial = (2, 1)
        heap = BinaryHeap(initial)
        heap.bubble_up(1)
        self.assertEqual(heap.value_list, [1, 2])

    def test_bubble_up_2(self):
        initial = (7, 6, 5, 4, 3, 2, 1)
        heap = BinaryHeap(initial)
        heap.bubble_up(6)
        self.assertEqual(heap.value_list, [1, 6, 7, 4, 3, 2, 5])

    def test_index_priority(self):
        heap = BinaryHeap((2, 1))
        self.assertEqual(heap.index_priority(0, 1), 1)
        self.assertEqual(heap.index_priority(1, 0), -1)

    def test_prioritize_indices(self):
        heap = BinaryHeap((5, 3, 1, 2, 4))
        self.assertEqual(heap.prioritize_indices(range(5)), [2, 3, 1, 4, 0])

    def test_bubble_down_1(self):
        heap = BinaryHeap((2, 1, 3))
        heap.bubble_down(0)
        self.assertEqual(heap.value_list, [1, 2, 3])

    def test_bubble_down_2(self):
        heap = BinaryHeap((10, 10, 9, 3, 4, 7 , 6, 1, 1, 1, 1, 11, 12, 13, 14))
        heap.bubble_down(0)
        self.assertEqual(heap.value_list, [9, 10, 6, 3, 4, 7, 10, 1, 1, 1, 1, 11, 12, 13, 14])

    def test_insert_1(self):
        heap = BinaryHeap()
        heap.insert(1)
        self.assertEqual(heap.value_list, [1])

    def test_insert_2(self):
        heap = BinaryHeap((1, 3))
        heap.insert(2)
        self.assertEqual(heap.value_list, [1, 3, 2])

    def test_insert_3(self):
        heap = BinaryHeap((4, 5, 6, 7, 8, 9))
        heap.insert(1)
        self.assertEqual(heap.value_list, [1, 5, 4, 7, 8, 9, 6])

    def test_delete_1(self):
        heap = BinaryHeap((1, 2))
        heap.delete(1)
        self.assertEqual(heap.value_list, [1])

    def test_delete_2(self):
        heap = BinaryHeap((1, 2, 3, 4, 5, 6, 7, 8))
        heap.delete(2)
        self.assertEqual(heap.value_list, [1, 2, 6, 4, 5, 8, 7])

    def test_pop_1(self):
        heap = BinaryHeap((1,))
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.value_list, [])

    def test_pop_2(self):
        heap = BinaryHeap((1, 2, 3, 4, 5, 6))
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.value_list, [2, 4, 3, 6, 5])
