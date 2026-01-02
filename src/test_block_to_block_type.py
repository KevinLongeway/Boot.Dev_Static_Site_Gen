import unittest
from src.block_types import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    # HEADING TESTS
    def test_heading_level_1(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_level_6(self):
        block = "###### Six levels"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_invalid_heading_no_spec(self):
        block = "###NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # CODE BLOCK TESTS
    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_single_line(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    # QUOTE TESTS
    def  test_quote_block(self):
        block = "> line one\n> line two"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_invalid_quote_block(self):
        block = "> valid\nnot valid"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # UNORDERED LIST TESTS
    def test_unordered_list(self):
        block = "- item one\n item two"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list(self):
        block = "- item one\nnot a list"
        self.assertEqual(block_to_block_type(block), BlockType. PARAGRAPH)

    # ORDERED LIST TESTS
    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_invalid_ordered_list_wrong_numbers(self):
        block = "1. first\n3. wrong"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # PARAGRAPH TESTS
    def test_paragraphj_single_line(self):
        block = "Just a normal paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph_multi_line(self):
        block = "Line one\nLine two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
