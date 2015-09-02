from MyStack import MyStack

class StacksOfPlates(MyStack):
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = MyStack()
        self.lengths = MyStack()

    def isEmpty(self):
        return self.stacks.isEmpty()

    def peek(self):
        latest_stack = self.stacks.peek()
        if latest_stack is None:
            return None
        return latest_stack.peek()

    def pop(self):
        latest_stack = self.stacks.peek()
        if latest_stack is None:
            raise Error("Stack already empty. Underflow?")

        result = latest_stack.pop()

        if latest_stack.isEmpty():
            self.stacks.pop()
            self.lengths.pop()
        else:
            self.lengths.push(self.lengths.pop() - 1)

        return result

    def push(self, item):
        latest_length = self.lengths.peek()

        if (latest_length is None) or (latest_length == self.threshold):
            new_stack = MyStack()
            new_stack.push(item)
            self.stacks.push(new_stack)
            self.lengths.push(1)
        else:
            latest_stack = self.stacks.peek()
            latest_stack.push(item)
            self.lengths.push(self.lengths.pop() + 1)



# TESTS
import unittest

class StacksOfPlatesTests(unittest.TestCase):
    def test_1(self):
        stacks = StacksOfPlates(5)
        self.assertTrue(stacks.isEmpty())
        for j in range(98):
            stacks.push(j)
        self.assertEqual(stacks.peek(), 97)
        self.assertEqual(stacks.lengths.peek(), 3)
        self.assertEqual(len(stacks.lengths.base), 20)
        self.assertEqual(len(stacks.stacks.base), 20)
        self.assertFalse(stacks.isEmpty())

        for j in range(50):
            self.assertEqual(stacks.pop(), 97-j)
        self.assertEqual(stacks.peek(), 47)
        self.assertEqual(stacks.lengths.peek(), 3)
        self.assertEqual(len(stacks.lengths.base), 10)
        self.assertEqual(len(stacks.stacks.base), 10)
