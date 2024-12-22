import unittest

from htmlnode import *

class test_leafnode(unittest.TestCase):
    def test_leaf1(self):
        leaf = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text</p>")
    def test_leaf2(self):
        leaf = LeafNode("b", "This is bold text")
        self.assertEqual(leaf.to_html(), "<b>This is bold text</b>")
    def test_leaf3(self):
        leaf = LeafNode("a", "This is a link", {"href": "google.com"})
        self.assertEqual(leaf.to_html(), "<a href='google.com'>This is a link</a>")



if __name__ == "__main__":
    unittest.main()
