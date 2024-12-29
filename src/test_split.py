from typing import Text
import unittest

from main import split_nodes_delimiter
from textnode import *

class test_split(unittest.TestCase):
    def test_node1(self):
        node1 = TextNode("This is `code` in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1], "`", TextType.Code)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("code", TextType.Code), TextNode(" in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)
    def test_node2(self):
        node1 = TextNode("This is *italic* in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1], "*", TextType.Italic)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("italic", TextType.Italic), TextNode(" in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)
    def test_node3(self):
        node1 = TextNode("This is **bold** in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1], "**", TextType.Bold)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("bold", TextType.Bold), TextNode(" in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)
    def test_node4(self):
        node1 = TextNode("This is `code`, *italic*, **bold**, `code` in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1], "`", TextType.Code)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("code", TextType.Code),TextNode(", *italic*, **bold**, ", TextType.Normal), TextNode("code", TextType.Code), TextNode(" in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)
    def test_node5(self):
        node1 = TextNode("This is **bold** in normal text", TextType.Normal)
        node2 = TextNode("This is *italic* in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1, node2], "**", TextType.Bold)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("bold", TextType.Bold), TextNode(" in normal text", TextType.Normal), TextNode("This is *italic* in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)
    def test_node6(self):
        node1 = TextNode("This is bold text", TextType.Bold)
        split_node = split_nodes_delimiter([node1], "*", TextType.Italic)
        expected_result = [TextNode("This is bold text", TextType.Bold)]
        self.assertEqual(split_node, expected_result)

if __name__ == "__main__":
    unittest.main()
