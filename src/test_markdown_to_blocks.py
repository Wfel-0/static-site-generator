import unittest

from main import markdown_to_blocks
from textnode import *

class test_markdown_to_blocks(unittest.TestCase):
    def test1(self):
        text = f"#This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ans = markdown_to_blocks(text)
        comp = ['#This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(ans, comp)
