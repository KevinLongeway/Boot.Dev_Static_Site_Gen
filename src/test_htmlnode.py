import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode("a", "click", None, {"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "click", None, {
            "href": "https://google.com",
            "target": "_blank"
        })
        result = node.props_to_html()
        # Order doesn't matter, so check both possibilities
        self.assertTrue(
            result == ' href="https://google.com" target="_blank"' or
            result == ' target="_blank" href="https://google.com"'
        )

if __name__ == "__main__":
    unittest.main()

