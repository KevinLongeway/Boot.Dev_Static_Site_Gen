
def markdown_to_blocks(markdown: str) -> list[str]:
    # Split to double newlines
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        cleaned = block.strip()
        if cleaned:   # ignore empty blocks
            blocks.append(cleaned)

    return blocks
