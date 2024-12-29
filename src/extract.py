import re

from textnode import *

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_link(old_nodes):
    ans = []
    for node in old_nodes:
        if node.text_type != TextType.Normal:
            ans.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            ans.append(node)
            continue
        for link in links:
            splited = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splited) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if splited[0] != "":
                ans.append(TextNode(splited[0], TextType.Normal))
            ans.append(TextNode(link[0], TextType.Links, link[1]))
            text = splited[1]
        if text != "":
            ans.append(TextNode(text, TextType.Normal))
    return ans


def split_nodes_image(old_nodes):
    ans = []
    for node in old_nodes:
        if node.text_type != TextType.Normal:
            ans.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            ans.append(node)
            continue
        for image in images:
            splited = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splited) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if splited[0] != "":
                ans.append(TextNode(splited[0], TextType.Normal))
            ans.append(TextNode(image[0], TextType.Images, image[1]))
            text = splited[1]
        if text != "":
            ans.append(TextNode(text, TextType.Normal))
    return ans


def split_nodes_link2(old_nodes):
    all_splited = []
    all_types = []
    ans = []
    all_links = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        all_links.extend(links)
        for link in links:
            splited = node.text.split(f"[{link[0]}]({link[1]})")
            all_splited.extend(splited)
        for i in all_splited:
            all_types.append(node.text_type)
    for i in range(len(all_splited)):
        ans.append(TextNode(all_splited[i], all_types[i]))
        if i < len(all_splited)-1:
            ans.append(TextNode(all_links[i][0], TextType.Links, all_links[i][1]))
    return ans
