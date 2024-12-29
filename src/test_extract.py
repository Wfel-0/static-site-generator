import unittest

from extract import *
from textnode import *

class test_extract(unittest.TestCase):
    def test_image1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        ans = extract_markdown_images(text)
        comp = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(ans, comp)
    def test_link1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        ans = extract_markdown_links(text)
        comp = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(ans, comp)
    def test_split_nodes_image(self):
        node1 = TextNode("Here is an image ![google](www.google.com) and that is it", TextType.Normal)
        ans = split_nodes_image([node1])
        comp = [TextNode("Here is an image ", TextType.Normal), TextNode("google", TextType.Images, "www.google.com"), TextNode(" and that is it", TextType.Normal)]
        self.assertEqual(ans, comp)
    def test_split_nodes_link(self):
        node1 = TextNode("Here is an image [google](www.google.com) and that is it", TextType.Normal)
        ans = split_nodes_link([node1])
        comp = [TextNode("Here is an image ", TextType.Normal), TextNode("google", TextType.Links, "www.google.com"), TextNode(" and that is it", TextType.Normal)]
        self.assertEqual(ans, comp)
    def test_split_nodes_link2(self):
        node1 = TextNode("Here is an image [google](www.google.com) and that is it", TextType.Normal)
        node2 = TextNode("Here is an image [google](www.google.com) and that is it", TextType.Normal)
        ans = split_nodes_link([node1, node2])
        comp = [TextNode("Here is an image ", TextType.Normal), TextNode("google", TextType.Links, "www.google.com"), TextNode(" and that is it", TextType.Normal), TextNode("Here is an image ", TextType.Normal), TextNode("google", TextType.Links, "www.google.com"), TextNode(" and that is it", TextType.Normal)]
        self.assertEqual(ans, comp)
    def test_split_nodes_link3(self):
        node1 = TextNode("Here is an image [google](www.google.com), [youtube](www.youtube.com) and that is it", TextType.Normal)
        ans = split_nodes_link([node1])
        comp = [TextNode("Here is an image ", TextType.Normal), TextNode("google", TextType.Links, "www.google.com"), TextNode(", ", TextType.Normal), TextNode("youtube", TextType.Links, "www.youtube.com"), TextNode(" and that is it", TextType.Normal)]
        self.assertEqual(ans, comp)




if __name__ == "__main__":
    unittest.main()
