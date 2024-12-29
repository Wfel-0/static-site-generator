from extract import split_nodes_image, split_nodes_link
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
        case _:
            raise ValueError("wrong type")
            #return LeafNode(None, text_node.text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for i in old_nodes:
        if i.text_type != TextType.Normal:
            new_nodes.append(i)
        else:
            temp_iter = i.text.split(delimiter)
            for j in range(len(temp_iter)):
                if j % 2 == 0:
                    new_nodes.append(TextNode(temp_iter[j], TextType.Normal))
                elif j % 2 != 0:
                    new_nodes.append(TextNode(temp_iter[j], text_type))
    return new_nodes

def text_to_textnodes(text):
    return split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(text, "**", TextType.Bold), "*", TextType.Italic), "`", TextType.Code)))

def markdown_to_blocks(markdown):
    all_blocks = []
    block = ""
    counter = 0
    ans = []
    for letter in markdown:
        if counter == 1 and letter == "\n":
            all_blocks.append(block)
            block = ""
            counter = 0
            continue
        elif letter == "\n":
            counter += 1
        elif counter == 1 and letter != "\n":
            counter = 0
        block += letter
    all_blocks.append(block)
    for bl in all_blocks:
        ans.append(bl.strip())
    return ans



main()
