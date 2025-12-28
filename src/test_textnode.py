import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_test_type(self):
        node = TextNode("Same text", TextType.TEXT)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("Link", TextType.LINKS, "https://a.com")
        node2 = TextNode("Link", TextType.LINKS, "https://b.com")
        self.assertNotEqual(node, node2)

    def test_equal_with_none_url(self):
        node = TextNode("No URL", TextType.TEXT)
        node2 = TextNode("No URL", TextType.TEXT, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
