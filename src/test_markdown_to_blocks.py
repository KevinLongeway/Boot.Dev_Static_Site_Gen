import unittest
from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        md = "This is a single block"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["This is a single block"])

    def test_three_blocks(self):
        md = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n"
            "- This is the first list item in a list block\n"
            "- This is a list item\n"
            "- This is another list item"
        )
        result = markdown_to_blocks(md)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "# This is a heading")
        self.assertEqual(result[1], "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.")
        self.assertEqual(
             result[2],
             "- This is the first list item in a list block\n"
             "- This is a list item\n"
             "- This is another list item"
        )

    def test_strips_whitespace(self):
        md = "    Block one    \n\n    Block two    "
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Block one", "Block two"])

    def test_ignores_empty_blocks(self):
        md = "Block one\n\n\n\nBlock two"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Block one", "Block two"])

    def test_multiline_paragraph(self):
        md = (
            "Line one\n"
            "Line two\n\n"
            "Next block"
        )
        result = markdown_to_blocks(md)

        self.assertEqual(result[0], "Line one\nLine two")
        self.assertEqual(result[1], "Next block")

if __name__ == "__main__":
    unittest.main()
