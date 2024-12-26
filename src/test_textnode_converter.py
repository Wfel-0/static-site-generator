import unittest

from htmlnode import LeafNode
from main import text_node_to_html_node
from textnode import TextNode, TextType

class test_converter(unittest.TestCase):
    def test_node1(self):
        node = TextNode("this is plain text", TextType.Normal)
        conv_node = text_node_to_html_node(node)
        eq_node = LeafNode(None, "this is plain text")
        self.assertEqual(conv_node.to_html(), eq_node.to_html())
    def test_node2(self):
        node = TextNode("this is a link", TextType.Links, "google.com")
        conv_node = text_node_to_html_node(node)
        eq_node = LeafNode("a", "this is a link", {"href": "google.com"})
        self.assertEqual(conv_node.to_html(), eq_node.to_html())
    def test_node3(self):
        node = TextNode("this is bold text", TextType.Bold)
        conv_node = text_node_to_html_node(node)
        eq_node = LeafNode("b", "this is bold text")
        self.assertEqual(conv_node.to_html(), eq_node.to_html())
