from graphs import BinaryTreeVertex

def balance_info(vertex):
    if vertex is None:
        return (True, 0)
    else:
        left_info = balance_info(vertex.left)
        if not left_info[0]:
            return False

        right_info = balance_info(vertex.right)
        is_balanced = right_info[0] and (-1 <= left_info[1] - right_info[1] <= 1)
        height = 1 + max(left_info[1], right_info[1])
        return (is_balanced, height)

def is_balanced(root):
    return balance_info(root)[0]



# TESTS
import unittest

class is_balancedTests(unittest.TestCase):
    def test_1(self):
        l = BinaryTreeVertex('l')
        r = BinaryTreeVertex('r')

        balanced_root = BinaryTreeVertex('root', l, r)
        self.assertTrue(is_balanced(balanced_root))

        left_leaning_root = BinaryTreeVertex('root', left=l, right=None)
        self.assertTrue(is_balanced(left_leaning_root))

        right_leaning_root = BinaryTreeVertex('root', left=None, right=r)
        self.assertTrue(is_balanced(right_leaning_root))

    def test_2(self):
        ll = BinaryTreeVertex('ll')
        lr = BinaryTreeVertex('lr')
        rl = BinaryTreeVertex('rl')
        rr = BinaryTreeVertex('rr')
        l = BinaryTreeVertex('l', ll, lr)
        r = BinaryTreeVertex('r', rl, rr)

        balanced_root = BinaryTreeVertex('root', l, r)
        self.assertTrue(is_balanced(balanced_root))

        left_leaning_root = BinaryTreeVertex('root', left=l, right=None)
        self.assertFalse(is_balanced(left_leaning_root))

        right_leaning_root = BinaryTreeVertex('root', left=None, right=r)
        self.assertFalse(is_balanced(right_leaning_root))

    def test_3(self):
        lll = BinaryTreeVertex('lll')
        llr = BinaryTreeVertex('llr')
        ll = BinaryTreeVertex('ll', lll, llr)
        lr = BinaryTreeVertex('lr')
        l = BinaryTreeVertex('l', ll, lr)

        rrr = BinaryTreeVertex('rrr')
        rr = BinaryTreeVertex('rr', right=rrr)
        r = BinaryTreeVertex('r', right=rr)

        root = BinaryTreeVertex('root', l, r)

        self.assertFalse(is_balanced(root))

