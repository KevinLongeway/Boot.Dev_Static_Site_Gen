import unittest
from block_types import BlockType, block_to_block_type
from block_to_html import block_to_html

class TestBlockToHtml(unittest.TestCase):

    def test_paragraph(self):
        md = "This is a paragraph."
        html = block_to_html(md)
        self.assertEqual(html, "<p>This is a paragraph.</p>")

    def test_heading_h1(self):
        md = "# Hello"
        html = block_to_html(md)
        self.assertEqual(html, "<h1>Hello</h1>")

    def test_heading_h3(self):
        md = "### Title"
        html = block_to_html(md)
        self.assertEqual(html, "<h3>Title</h3>")

    def test_code_block(self):
        md = "```\nprint('hi')\n```"
        html = block_to_html(md)
        self.assertEqual(html, "<pre><code>print('hi')</code></pre>")

    def test_quote_block(self):
        md = "> hello\n> world"
        html = block_to_html(md)
        self.assertEqual(html, "<blockquote>hello\nworld</blockquote>")

    def test_unordered_list(self):
        md = "- apple\n- banana\n- cherry"
        html = block_to_html(md)
        self.assertEqual(html, "<ul><li>apple</li><li>banana</li><li>cherry</li></ul>")

    def test_ordered_list(self):
        md = "1. first\n2. second\n3. third"
        html = block_to_html(md)
        self.assertEqual(html, "<ol><li>first</li><li>second</li><li>third</li></ol>")

    def test_block_type_detection(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("plain text"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
