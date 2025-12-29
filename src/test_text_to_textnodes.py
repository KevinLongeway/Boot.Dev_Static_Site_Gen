import unittest
from src.textnode import TextNode, TextType
from src.text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_plain_text(self):
        text = "Just plain text"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Just plain text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_bold_text(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_italic_text(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)

    def test_code_text(self):
        text = "Inline `code` example"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_image(self):
        text = "Look at this ![cat](a.png)"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].text, "cat")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "a.png")

    def test_link(self):
        text = "Go to [Boot.dev](https://www.boot.dev)"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].text, "Boot.dev")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://www.boot.dev")

    def test_multiple_markdown(self):
        text = "Hello **bold** _italic_ `code`"
        result = text_to_textnodes(text)

        # Expect: TEXT, BOLD, TEXT, ITALIC, TEXT, CODE
        types = [node.text_type for node in result]
        self.assertEqual(
            types,
            [
                TextType.TEXT,
                TextType.BOLD,
                TextType.TEXT,
                TextType.ITALIC,
                TextType.TEXT,
                TextType.CODE,
            ]
        )

    def test_mixed_images_links_and_text(self):
        text = "A ![img](a.png) and [link](b.com)"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "A ")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text_type, TextType.LINK)

    def test_no_markdown(self):
        text = "Nothing special here"
        result = text_to_textnodes(text)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Nothing special here")
        self.assertEqual(result[0].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()
