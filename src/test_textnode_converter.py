import unittest

from htmlnode import LeafNode
from main import text_node_to_html_node
from textnode import TextNode, TextType

class test_converter(unittest.TestCase):
    def test_node1(self):
        node = TextNode("this is plain text", TextType.Normal)
        conv_node = text_node_to_html_node(node)
        eq_node = LeafNode(None, "this is plain text")
        self.assertEqual(conv_node, eq_node)
