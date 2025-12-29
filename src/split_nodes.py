from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_images, extract_markdown_links
from src.split_delimiter import split_nodes_delimiter

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only Split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        # If no images, keep node unchanged
        if not images:
            new_nodes.append(node)
            continue

        # Process each image in order
        for alt, url in images:
            markdown = f"![{alt}]({url})"
            parts = text.split(markdown, 1)

            # text before the image
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # the image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            # continue processing the rest of the text
            text = parts[1]

        # leftover text after last image
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for label, url in links:
            markdown = f"[{label}]({url})"
            parts = text.split(markdown, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(label, TextType.LINK, url))

            text = parts[1]

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
