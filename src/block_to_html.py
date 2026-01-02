from block_types import BlockType, block_to_block_type

def block_to_html(block: str) -> str:
    block_type = block_to_block_type(block)
    lines = block.split("\n")

    # Paragraph
    if block_type == BlockType.PARAGRAPH:
        return f"<p>{block}</p>"

    # Heading
    if block_type == BlockType.HEADING:
        first = lines[0]
        level = 0
        for c in first:
            if c == "#":
                level += 1
            else:
                break
        text = first[level+1:]   # skip #'s and the space
        return f"<h{level}>{text}</h{level}>"

    # Code Block
    if block_type == BlockType.CODE:
        inner = "\n".join(lines[1:-1])
        return f"<pre><code>{inner}</code></pre>"

    # Quote Block
    if block_type == BlockType.QUOTE:
        cleaned = "\n".join(line[1:].lstrip() for line in lines)
        return f"<blockquote>{cleaned}</blockquote>"

    # Unordered List
    if block_type == BlockType.UNORDERED_LIST:
        items = []
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith("- "):
                items.append(stripped[2:])
        lis = "".join(f"<li>{item}</li>" for item in items)
        return f"<ul>{lis}</ul>"

    # Ordered List
    if block_type == BlockType.ORDERED_LIST:
        items = []
        for line in lines:
            # remove "1. ", "2. ", ....
            parts = line.split(". ", 1)
            if len(parts) == 2:
                items.append(parts[1])
        lis = "".join(f"<li>{item}</li>" for item in items)
        return f"<ol>{lis}</ol>"

    raise ValueError("Unknown block type")
