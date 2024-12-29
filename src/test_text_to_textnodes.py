import unittest

from main import text_to_textnodes
from textnode import *

class test_text_to_textnodes(unittest.TestCase):
    def test1(self):
        text = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.Normal)
        ans = text_to_textnodes([text])
        comp = [
            TextNode("This is ", TextType.Normal),
            TextNode("text", TextType.Bold),
            TextNode(" with an ", TextType.Normal),
            TextNode("italic", TextType.Italic),
            TextNode(" word and a ", TextType.Normal),
            TextNode("code block", TextType.Code),
            TextNode(" and an ", TextType.Normal),
            TextNode("obi wan image", TextType.Images, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.Normal),
            TextNode("link", TextType.Links, "https://boot.dev"),
        ]
        self.assertEqual(ans, comp)

    def test2(self):
        text = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.Normal)
        text2 = TextNode("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.Normal)
        ans = text_to_textnodes([text, text2])
        comp = [
            TextNode("This is ", TextType.Normal),
            TextNode("text", TextType.Bold),
            TextNode(" with an ", TextType.Normal),
            TextNode("italic", TextType.Italic),
            TextNode(" word and a ", TextType.Normal),
            TextNode("code block", TextType.Code),
            TextNode(" and an ", TextType.Normal),
            TextNode("obi wan image", TextType.Images, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.Normal),
            TextNode("link", TextType.Links, "https://boot.dev"),
            TextNode("This is ", TextType.Normal),
            TextNode("text", TextType.Bold),
            TextNode(" with an ", TextType.Normal),
            TextNode("italic", TextType.Italic),
            TextNode(" word and a ", TextType.Normal),
            TextNode("code block", TextType.Code),
            TextNode(" and an ", TextType.Normal),
            TextNode("obi wan image", TextType.Images, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.Normal),
            TextNode("link", TextType.Links, "https://boot.dev"),
        ]
        self.assertEqual(ans, comp)


if __name__ == "__main__":
    unittest.main()
