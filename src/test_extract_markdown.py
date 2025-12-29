import unittest
from src.extract_markdown import extract_markdown_images, extract_markdown_links

class test_extract_single_image(unittest.TestCase):
    def test_extract_single_image(self):
        text = "Here is an image ![alt text](https://example.com/img.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "https://example.com/img.png")])

    def test_extract_multiple_images(self):
        text = ("First ![one](https://a.com/a.png) and Second ![two](https://b.com/b.png)")
        result = extract_markdown_images(text)
        self.assertEqual(result, [("one", "https://a.com/a.png"),("two", "https://b.com/b.png"),])

    def test_extract_single_link(self):
        text = "Visit [Boot.dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("Boot.dev", "https://www.boot.dev")])

    def test_extract_multiple_links(self):
        text = ("Links: [Google](https://google.com) and [YouTube](https://YouTube.com)")
        result = extract_markdown_links(text)
        self.assertEqual(result, [("Google", "https://google.com"),("YouTube", "https://YouTube.com")])

    def test_links_do_not_capture_images(self):
        text = "![pic](https://img.com/x.png) and [link](https://site.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://site.com")])

    def test_no_images(self):
        text = "No images here"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_no_links(self):
        text = "No links here"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()

