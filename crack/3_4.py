from MyStack import MyStack


class MyQueue(object):
    def __init__(self):
        self._enstack = MyStack()
        self._destack = MyStack()
        self._mode = "ENQUEUE"

    def isEmpty(self):
        return self._enstack.isEmpty() and self._destack.isEmpty()

    def _shift(self, source, target):
        while not source.isEmpty():
            target.push(source.pop())

    def _enmode(self):
        if self._mode == "DEQUEUE":
            self._shift(self._destack, self._enstack)
            self._mode = "ENQUEUE"

    def _demode(self):
        if self._mode == "ENQUEUE":
            self._shift(self._enstack, self._destack)
            self._mode = "DEQUEUE"

    def enqueue(self, item):
        self._enmode()
        self._enstack.push(item)

    def dequeue(self):
        self._demode()
        return self._destack.pop()

    def peek(self):
        self._demode()
        return self._destack.peek()



# TESTS
import unittest

class MyQueueTests(unittest.TestCase):
    def test_1(self):
        q = MyQueue()
        self.assertTrue(q.isEmpty())

        q.enqueue(0)
        self.assertEqual(q._mode, "ENQUEUE")
        self.assertEqual(q.peek(), 0)
        self.assertEqual(q._mode, "DEQUEUE")

        q.enqueue(1)
        self.assertEqual(q._mode, "ENQUEUE")
        self.assertEqual(q.peek(), 0)
        self.assertEqual(q._mode, "DEQUEUE")

        item = q.dequeue()
        self.assertEqual(item, 0)
        self.assertEqual(q._mode, "DEQUEUE")
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q._mode, "DEQUEUE")

        q.enqueue(2)
        self.assertEqual(q._mode, "ENQUEUE")
        for j in range(2):
            self.assertEqual(q.dequeue(), j+1)
            self.assertEqual(q._mode, "DEQUEUE")
