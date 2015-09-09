"""
A Trie implementation.

The root has value "" and the leaves have value "TERMINAL"
"""

class Trie(object):
    def __init__(self):
        self.root = TrieVertex("")

    def traverse(self, prefix):
        current = self.root
        for i in range(len(prefix)):
            try:
                current = current.children[prefix[i]]
            except KeyError:
                return None
        return current

    def contains(self, word):
        matcher = self.traverse(word)
        if matcher is None:
            return False
        elif "TERMINAL" in matcher.children:
            return True
        else:
            return False

    def insert(self, word):
        current = self.root
        for i in range(len(word)):
            character = word[i]
            if character not in current.children:
                current.extend(character)
            current = current.children[character]
        current.extend("TERMINAL")

    def complete(self, prefix):
        jump = self.traverse(prefix)
        if jump is None:
            return None

        suffices = jump.suffices()
        completions = [prefix + suffix for suffix in suffices]
        return completions


class TrieVertex(object):
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child):
        self.children[child.value] = child

    def extend(self, value):
        child = TrieVertex(value)
        self.add_child(child)
        return child

    def suffices(self):
        value = self.value

        if value == "TERMINAL" or len(self.children) == 0:
            return [""]

        s = []
        for key, child in self.children.items():
            if child.value == "TERMINAL":
                s.append("")
                continue
            for suffix in child.suffices():
                s.append(child.value + suffix)

        return s


# TESTS
import unittest

class TrieTests(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_constructor(self):
        trie = self.trie
        self.assertEqual(trie.root.value, "")
        self.assertEqual(trie.root.children, {})

    def test_insert_1(self):
        trie = self.trie
        trie.insert("abba")

        empty = trie.root
        self.assertIn("a", empty.children)
        first = empty.children["a"]
        self.assertIn("b", first.children)
        second = first.children["b"]
        self.assertIn("b", second.children)
        third = second.children["b"]
        self.assertIn("a", third.children)
        fourth = third.children["a"]
        self.assertIn("TERMINAL", fourth.children)

    def test_insert_2(self):
        trie = self.trie
        trie.insert("ab")
        trie.insert("cd")

        empty = trie.root
        self.assertIn("a", empty.children)
        self.assertIn("c", empty.children)

        a = empty.children["a"]
        self.assertIn("b", a.children)
        self.assertIn("TERMINAL", a.children["b"].children)

        c = empty.children["c"]
        self.assertIn("d", c.children)
        self.assertIn("TERMINAL", c.children["d"].children)

    def test_insert_3(self):
        trie = self.trie
        trie.insert("lo")
        trie.insert("la")

        self.assertEqual(len(trie.root.children), 1)
        self.assertIn("l", trie.root.children)
        self.assertIn("o", trie.root.children["l"].children)
        self.assertIn("a", trie.root.children["l"].children)

    def test_traverse(self):
        trie = self.trie
        trie.insert("lazy")
        trie.insert("pepper")
        trie.insert("cat")
        trie.insert("lap")

        destination = trie.traverse("la")
        self.assertEqual(destination.value, "a")
        self.assertIs(destination, trie.root.children["l"].children["a"])

    def test_contains(self):
        trie = self.trie
        trie.insert("wow")
        trie.insert("rofl")

        self.assertTrue(trie.contains("wow"))
        self.assertTrue(trie.contains("rofl"))
        self.assertFalse(trie.contains("lol"))

    def test_complete(self):
        trie = self.trie
        trie.insert("wtf")
        trie.insert("omg")
        trie.insert("wow")

        self.assertEqual(set(trie.complete("w")), {"wtf", "wow"})
        self.assertEqual(trie.complete("om"), ["omg"])
        self.assertIsNone(trie.complete("a"))


class TrieVertexTests(unittest.TestCase):
    def test_constructor(self):
        v = TrieVertex("v")
        self.assertEqual(v.value, "v")
        self.assertEqual(v.children, {})

    def test_add_child(self):
        v = TrieVertex("v")
        w = TrieVertex("w")
        v.add_child(w)

        self.assertIn(w.value, v.children)
        self.assertEqual(v.children[w.value], w)

    def test_extend(self):
        v = TrieVertex("v")
        extension = "w"
        v.extend(extension)

        self.assertIn(extension, v.children)
        self.assertEqual(v.children[extension].value, extension)

    def test_suffices_1(self):
        v = TrieVertex("v")
        suffices = v.suffices()
        self.assertEqual(suffices, [""])

    def test_suffices_2(self):
        v = TrieVertex("v")
        v.extend("w")
        v.extend("x")
        v.extend("y")
        v.extend("z")

        suffices = v.suffices()

        self.assertEqual(set(suffices), {"w", "x", "y", "z"})

    def test_suffices_3(self):
        a = TrieVertex("a")
        l = TrieVertex("l")
        o = TrieVertex("o")
        z = TrieVertex("z")

        l.add_child(o)
        o.extend("l")

        l.add_child(a)
        a.extend("p")
        a.add_child(z)
        z.extend("y")

        suffices = l.suffices()
        self.assertEqual(set(suffices), {"ol", "ap", "azy"})
