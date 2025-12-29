from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if self.children is None:
            raise ValueError("Children value must not be None")

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props = self.props_to_html()

        return f"<{self.tag}{props}>{children_html}</{self.tag}>"
