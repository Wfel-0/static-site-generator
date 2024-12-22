import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node,node2)
    
    def test_eq2(self):
        node = TextNode("Lorem ipsum...", TextType.Italic)
        node2 = TextNode("Lorem ipsum...", TextType.Italic)
        self.assertEqual(node,node2)

    def test_eq3(self):
        node = TextNode("Lorem ipsum...", TextType.Code)
        node2 = TextNode("Lorem ipsum...", TextType.Code)
        self.assertEqual(node,node2)

    def test_eq4(self):
        node = TextNode("Lorem ipsum...", TextType.Normal)
        node2 = TextNode("Lorem ipsum...", TextType.Normal)
        self.assertEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
