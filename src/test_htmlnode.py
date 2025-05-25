import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props = {"href": "https://www.google.com",
                         "target": "_blank"})
        self.assertEqual(node.props_to_html(),  "href=\"https://www.google.com\" target=\"_blank\"")
    def test_repr(self):
        node = HTMLNode(props = {}, value = "text", tag = "p")
        node2 = HTMLNode(props = {}, value = "text", tag = "p")
        self.assertEqual(node.__repr__(), "HTMLNODE(p, text, None, {})")
    def test_empty_props(self):
        node = HTMLNode(props = {})
        self.assertEqual(node.props_to_html(), "")  
    def test_none_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")   


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()
