from MyStack import MyStack


def sort_stack(stack):
    sorter = MyStack()
    while not stack.isEmpty():
        holder = stack.pop()

        if sorter.isEmpty():
            sorter.push(holder)
        else:
            counter = 0
            while (not sorter.isEmpty()) and (sorter.peek() > holder):
                stack.push(sorter.pop())

            sorter.push(holder)

            for _ in range(counter):
                sorter.push(stack.pop())

    while not sorter.isEmpty():
        stack.push(sorter.pop())



# TESTS
import unittest


class sort_stackTests(unittest.TestCase):
    def test_1(self):
        items = [2, 3, 4, 5, 1, 3, 5, 7, 8, 2, 9]
        stack = MyStack()
        for item in items:
            stack.push(item)
        sort_stack(stack)

        result = []
        while not stack.isEmpty():
            result.append(stack.pop())
        self.assertEqual(result, sorted(items))
