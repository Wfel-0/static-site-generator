from textnode import *
from htmlnode import *

def main():
    obj = TextNode("This is a text node", TextType.Bold, "https://www.boot.dev")
    print(obj)
    obj2 = HTMLNode("p", "zulty", ["a", "p", "h3"], {"href": "www.google.com", "method": "post"})
    print(obj2)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.Normal:
            return LeafNode(None, text_node.text)
        case TextType.Bold:
            return LeafNode("b", text_node.text)
        case TextType.Italic:
            return LeafNode("i", text_node.text)
        case TextType.Code:
            return LeafNode("code", text_node.text)
        case TextType.Links:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.Images:
            return LeafNode("img", None, {"src": text_node.url})




main()
