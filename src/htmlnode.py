


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def props_to_html(self):
        if self.props is None:
            return ""
        str = ""
        for i in self.props:
            str += f" {i}='{self.props[i]}'"
        return str

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def __repr__(self):
        return f"{self.tag}|{self.value}|{self.children}|{self.props}";

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is None")
        if self.children is None:
            raise ValueError("there are no children")
        str = ""
        for i in self.children:
            str += i.to_html()
        return f"<{self.tag}{self.props_to_html()}>{str}</{self.tag}>"
