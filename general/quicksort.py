"""
In-place quick sort implementation.

This implementation uses a low index moving up and a high index moving down at each step in order to figure out where to
partition the array. This is in contrast with the conventional implementation in which there is a single index moving
up the array and a separate index maintaining the position in which the pivot should be inserted.
"""
import copy


def quicksort(array, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if high <= low:
        return None

    pivot = copy.copy(array[low])
    inc = low + 1
    dec = high

    while inc <= dec:
        while dec >= low and array[dec] > pivot:
            dec -= 1
        while inc <= high and array[inc] <= pivot:
            inc += 1

        if inc < dec:
            temp = copy.copy(array[dec])
            array[dec] = array[inc]
            array[inc] = temp

    insertion = inc - 1
    array[low] = array[insertion]
    array[insertion] = pivot
    quicksort(array, low, insertion-1)
    quicksort(array, insertion+1, high)



# TESTS
import unittest

class quicksortTests(unittest.TestCase):
    def test_1(self):
        a = [1, 2, 3]
        quicksort(a)
        self.assertEqual(a, [1, 2, 3])

    def test_2(self):
        a = [2, 1, 3]
        quicksort(a)
        self.assertEqual(a, [1, 2, 3])

    def test_3(self):
        a = [2, 1, 2]
        quicksort(a)
        self.assertEqual(a, [1, 2, 2])

    def test_4(self):
        a = [1, 1, 1]
        quicksort(a)
        self.assertEqual(a, [1, 1, 1])

    def test_5(self):
        a = [4, 2, 3, 34, 53, 343124, 1]
        quicksort(a)
        self.assertEqual(a, [1, 2, 3, 4, 34, 53, 343124])

    def test_6(self):
        a = [-5, 0, -5, 1, 2, 3]
        quicksort(a)
        self.assertEqual(a, [-5, -5, 0, 1, 2, 3])
