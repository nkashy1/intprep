from MyStack import MyStack

class MinStack(MyStack):
    def __init__(self):
        self.stack = MyStack()
        self.mins = MyStack()

    def isEmpty(self):
        return self.stack.isEmpty()

    def peek(self):
        return self.stack.peek()

    def min(self):
        return self.mins.peek()

    def pop(self):
        self.mins.pop()
        return self.stack.pop()

    def push(self, item):
        current_min = self.min()
        if (current_min is None) or (item < current_min):
            self.mins.push(item)
        else:
            self.mins.push(current_min)

        self.stack.push(item)



# TESTS
import unittest

class MinStackTests(unittest.TestCase):
    def setUp(self):
        self.stack = MinStack()

        self.initial = range(10)
        self.initial.reverse()
        for i in self.initial:
            self.stack.push(i)

        for i in range(100):
            self.stack.push(i)

    def test_push(self):
        stack_base = self.stack.stack.base
        self.assertEqual(stack_base, self.initial + range(100))

        mins_base = self.stack.mins.base
        self.assertEqual(mins_base, self.initial + [0]*100)

    def test_min(self):
        for j in range(100):
            self.assertEqual(self.stack.min(), 0)
            self.stack.pop()
        for j in range(10):
            self.assertEqual(self.stack.min(), j)
            self.stack.pop()

    def test_pop(self):
        for j in range(100):
            self.assertEqual(self.stack.pop(), 99 - j)
        for j in range(10):
            self.assertEqual(self.stack.pop(), j)