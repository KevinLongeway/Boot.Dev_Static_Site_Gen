import unittest
from src.textnode import TextNode, TextType
from src.split_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)

        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_no_delimiter(self):
        node = TextNode("Nothing to split here", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Nothing to split here")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_multiple_delimiters(self):
        node = TextNode("Here is `code` and mode `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 4)
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[3].text_type, TextType.CODE)

    def test_ignore_non_text_nodes(self):
        node1 = TextNode("Normal text", TextType.TEXT)
        node2 = TextNode("Already bold", TextType.BOLD)

        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[1].text_type, TextType.BOLD)

    def test_raises_on_missing_closing_delimiter(self):
        node = TextNode("This is **broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()
