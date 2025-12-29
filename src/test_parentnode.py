import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_single_child(self):
        parent = ParentNode("p", [LeafNode(None, "Hello")])
        self.assertEqual(parent.to_html(), "<p>Hello</p>")

    def test_multiple_children(self):
        parent = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " text"),
            LeafNode("i", "italic")
        ])
        self.assertEqual(parent.to_html(), "<p><b>Bold</b> text<i>italic</i></p>")

    def test_nested_parent(self):
        inner = ParentNode("span", [LeafNode(None, "inside")])
        outer = ParentNode("div", [inner])
        self.assertEqual(outer.to_html(), "<div><span>inside</span></div>")

    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "text")]).to_html()

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()

if __name__== "__main__":
    unittest.main()
