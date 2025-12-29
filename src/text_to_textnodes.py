from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    # Start with a single TEXT node
    nodes = [TextNode(text, TextType.TEXT)]

    # Split bold (**)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # Split italic (_)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Split code (`code`)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Split images (![alt](url))
    nodes = split_nodes_image(nodes)

    # Split links ([text](url))
    nodes = split_nodes_link(nodes)

    return nodes
