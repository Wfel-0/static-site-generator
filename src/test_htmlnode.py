import unittest

from htmlnode import *

class test_htmlnode(unittest.TestCase):
    def test_prop(self):
        test_prop1 = HTMLNode("p", "zulty", ["a", "p", "h3"], {"href": "www.google.com", "method": "post"})
        test_str = "p|zulty|['a', 'p', 'h3']|{'href': 'www.google.com', 'method': 'post'}"
        self.assertEqual(repr(test_prop1), test_str)
    def test_prop2(self):
        test_prop1 = HTMLNode("h4", "zulty", ["a", "p", "h3"], {"href": "www.wp.pl", "method": "post"})
        test_str = "h4|zulty|['a', 'p', 'h3']|{'href': 'www.wp.pl', 'method': 'post'}"
        self.assertEqual(repr(test_prop1), test_str)
    def test_prop3(self):
        test_prop1 = HTMLNode("a", "zulty", ["a", "p", "h3"], {"href": "www.google.com", "method": "post"})
        test_str = "a|zulty|['a', 'p', 'h3']|{'href': 'www.google.com', 'method': 'post'}"
        self.assertEqual(repr(test_prop1), test_str)

class test_parentnode(unittest.TestCase):
    def test_parent(self):
        test_node = ParentNode("p", [LeafNode("p", "This is a paragraph of text"), LeafNode("p", "This is a paragraph of text")],)
        test_str = "<p><p>This is a paragraph of text</p><p>This is a paragraph of text</p></p>"
        self.assertEqual(test_node.to_html(), test_str)
    def test_parent2(self):
        test_node = ParentNode("b", [LeafNode("p", "This is a paragraph of text"), LeafNode("p", "This is a paragraph of text")],)
        test_str = "<b><p>This is a paragraph of text</p><p>This is a paragraph of text</p></b>"
        self.assertEqual(test_node.to_html(), test_str)
#    def test_parent3(self):
#        test_node = ParentNode("p", [LeafNode("p", "This is a paragraph of text"), ParentNode("p", [LeafNode("p", "This is a paragraph of text"), LeafNode("p", "This is a paragraph of text")])],)
#        test_str = "<p><p>This is a paragraph of text</p><p>This is a paragraph of text</p></p>"
#        self.assertEqual(test_node.to_html(), test_str)

if __name__ == "__main__":
    unittest.main()
