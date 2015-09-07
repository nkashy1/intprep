from graphs import BinaryTreeVertex

def list_of_children(vertex_list):
    children = []
    for v in vertex_list:
        if v.left is not None:
            children.append(v.left)

        if v.right is not None:
            children.append(v.right)

    return children

def list_of_depths(root):
    depth_list = {1: [root]}
    current_depth = 1
    children = list_of_children(depth_list[current_depth])

    while children != []:
        current_depth += 1
        depth_list[current_depth] = children
        children = list_of_children(children)

    return depth_list


# TESTS
import unittest

class list_of_depthsTests(unittest.TestCase):
    def test_1(self):
        ll = BinaryTreeVertex('ll')
        lr = BinaryTreeVertex('lr')
        rl = BinaryTreeVertex('rl')
        rr = BinaryTreeVertex('rr')
        l = BinaryTreeVertex('l', ll, lr)
        r = BinaryTreeVertex('r', rl, rr)
        root = BinaryTreeVertex('root', l, r)

        depth_list = list_of_depths(root)

        self.assertEqual(len(depth_list), 3)
        self.assertEqual(depth_list[1], [root])
        self.assertEqual(depth_list[2], [l, r])
        self.assertEqual(depth_list[3], [ll, lr, rl, rr])
