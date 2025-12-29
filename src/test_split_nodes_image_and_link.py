import unittest
from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodesImageAndLink(unittest.TestCase):

    # IMAGE TESTS
    def test_single_image(self):
        node = TextNode("Here is an ![cat](https://img.com/cat.png)", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Here is an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "cat")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://img.com/cat.png")

    def test_multiple_images(self):
        node = TextNode("One ![a](url1) Two ![b](url2) three", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(len(result), 5)

        self.assertEqual(result[0].text, "One ")
        self.assertEqual(result[1].text, "a")
        self.assertEqual(result[1].url, "url1")
        self.assertEqual(result[2].text, " Two ")
        self.assertEqual(result[3].text, "b")
        self.assertEqual(result[3].url, "url2")
        self.assertEqual(result[4].text, " three")

    def test_no_images(self):
        node = TextNode("Nothing here", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Nothing here")

    def test_non_text_nodes_pass_through_images(self):
        node = TextNode("already image", TextType.IMAGE, "url")
        result = split_nodes_image([node])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text_type, TextType.IMAGE)

    # LINK TESTS
    def test_single_link(self):
        node = TextNode("Go to [Boot.dev](https://www.boot.dev)", TextType.TEXT)
        result = split_nodes_link([node])


        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Go to ")
        self.assertEqual(result[1].text, "Boot.dev")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://www.boot.dev")

    def test_multiple_links(self):
        node = TextNode("Links: [A](url1) and [B](url2)", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Links: ")
        self.assertEqual(result[1].text, "A")
        self.assertEqual(result[1].url, "url1")
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "B")
        self.assertEqual(result[3].url, "url2")

    def test_no_links(self):
        node = TextNode("Nothing here", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Nothing here")

    def test_non_text_nodes_pass_through_links(self):
        node = TextNode("already link", TextType.LINK, "url")
        result = split_nodes_link([node])

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text_type, TextType.LINK)

if __name__ =="__main__":
    unittest.main()





