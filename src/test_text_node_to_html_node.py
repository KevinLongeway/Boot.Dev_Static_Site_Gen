import unittest
from src.textnode import TextNode, TextType
from src.htmlnode import text_node_to_html_node
from src.leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_text(self):
        node = TextNode("Hello", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "Hello")

    def test_text_type_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "<i>Italic text</i>")

    def test_text_type_code(self):
        node = TextNode("print('hi')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.to_html(), "<code>print('hi')</code>")

    def test_text_type_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html = text_node_to_html_node(node)
        self.assertEqual(
            html.to_html(),
            '<a href="https://boot.dev">Boot.dev</a>'
        )

    def test_text_type_image(self):
        node = TextNode("Boot logo", TextType.IMAGE, "https://boot.dev/logo.png")
        html = text_node_to_html_node(node)
        self.assertEqual(
            html.to_html(),
            '<img src="https://boot.dev/logo.png" alt="Boot logo"></img>'
        )

    def test_invalid_text_type_raises(self):
        class FakeType:
            pass

        node = TextNode("Bad", FakeType())
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()

