import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_null_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_ineq(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text_content_ineq(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a different text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url_content_eq(self):
        node = TextNode(
            "This is a text node", TextType.PLAIN, "https://www.example.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.PLAIN, "https://www.example.com"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextType.PLAIN, "https://www.example.com"
        )
        self.assertEqual(
            repr(node), "TextNode(This is a text node, plain, https://www.example.com)"
        )


if __name__ == "__main__":
    unittest.main()
