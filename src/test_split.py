import unittest

from main import split_nodes_delimiter
from textnode import *

class test_split(unittest.TestCase):
    def test_node1(self):
        node1 = TextNode("This is `code` in normal text", TextType.Normal)
        split_node = split_nodes_delimiter([node1], "`", TextType.Code)
        expected_result = [TextNode("This is ", TextType.Normal), TextNode("code", TextType.Code), TextNode(" in normal text", TextType.Normal)]
        self.assertEqual(split_node, expected_result)

