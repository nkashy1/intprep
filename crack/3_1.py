class ThreeInOneStack(object):
    def __init__(self, array_length):
        self.base = {}
        for i in range(array_length):
            self.base[i] = None

        self.bottoms = {}
        for r in range(3):
            self.bottoms[(array_length-r)%3] = array_length - 1 - r

        self.tops = {}
        for k in self.bottoms:
            self.tops[k] = self.bottoms[k] + 3

    def validate_stack_number(self, stack):
        if not (0 <= stack < 3):
            raise ValueError("Stack number must be 0, 1, or 2.")

    def isEmpty(self, stack):
        self.validate_stack_number(stack)
        return self.tops[stack] > self.bottoms[stack]

    def peek(self, stack):
        self.validate_stack_number(stack)
        if self.tops[stack] > self.bottoms[stack]:
            return None
        return self.base[self.tops[stack]]

    def push(self, stack, item):
        self.validate_stack_number(stack)
        top = self.tops[stack] - 3
        if top < 0:
            raise Error("Stack overflow. Always wanted to say that.")
        self.base[top] = item
        self.tops[stack] = top

    def pop(self, stack):
        self.validate_stack_number(stack)
        if self.tops[stack] > self.bottoms[stack]:
            raise Error("Stack already empty. Underflow?")
        result = self.base[self.tops[stack]]
        self.base[self.tops[stack]] = None
        self.tops[stack] += 3
        return result



# TESTS
import unittest


class ThreeInOneStackTests(unittest.TestCase):
    def setUp(self):
        self.stack = ThreeInOneStack(97)

    def test_construction(self):
        self.assertEqual(self.stack.bottoms[0], 95)
        self.assertEqual(self.stack.bottoms[1], 96)
        self.assertEqual(self.stack.bottoms[2], 94)

    def test_validate_stack_number(self):
        self.assertIsNone(self.stack.validate_stack_number(0))
        self.assertIsNone(self.stack.validate_stack_number(1))
        self.assertIsNone(self.stack.validate_stack_number(2))
        self.assertRaises(ValueError, self.stack.validate_stack_number, 1283)

    def test_isEmpty(self):
        for i in range(3):
            self.assertTrue(self.stack.isEmpty(i))
            self.stack.tops[i] -= 3
            self.assertFalse(self.stack.isEmpty(i))

    def test_peek(self):
        for i in range(3):
            self.stack.tops[i] -= 3
            self.stack.base[self.stack.tops[i]] = i
            self.assertEqual(self.stack.peek(i), i)

    def test_push(self):
        for j in range(31):
            for i in range(3):
                self.stack.push(i, j)
                self.assertEqual(self.stack.base[self.stack.bottoms[i] - 3*j], j)
                self.assertEqual(self.stack.tops[i], self.stack.bottoms[i] - 3*j)

    def test_pop(self):
        for j in range(31):
            for i in range(3):
                self.stack.push(i, j)

        for i in range(3):
            for j in range(31):
                result = self.stack.pop(i)
                self.assertEqual(result, 30-j)
