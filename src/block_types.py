from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Code Block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading
    if lines[0].startswith("#"):
        # Count leading #'s
        count = 0
        for c in lines[0]:
            if c == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and lines[0][count:].startswith(" "):
            return BlockType.HEADING

    # Quote Block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    has_bullet = False
    for line in lines:
        stripped = line.lstrip()

        if stripped == "":
            continue

        if stripped.startswith("- "):
            has_bullet = True
            continue
        # If a non-bullet line looks like another block type, reject
        if not line.startswith(" "):
            break
    else:
        # Loop ended normally -> no break -> valid unordered list
        if has_bullet:
            return BlockType.UNORDERED_LIST

    # Ordered list
    for i, line in enumerate(lines, start=1):
        prefix = f"{i}. "
        if not line.startswith(prefix):
            break
    else:
        return BlockType.ORDERED_LIST

    # Default
    return BlockType.PARAGRAPH
