class HTMLNode():
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        string = ""
        if self.props == None:
            return string
        for key in self.props:
            string += f"{key}=\"{self.props[key]}\" "
        return string[:-1]
    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if self.value == None or self.value == "": raise ValueError("to_html requires a value")
        if self.tag == None: return self.value
        if self.props == None or self.props == {}:
           return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag = None, children =None, props=None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):

        #print("to_html called on", self)
        if self.tag == None: raise ValueError("ParentNode requires tag")
        if self.children == None: raise ValueError("ParentNode requires children")
        s = f"<{self.tag}>"

        for node in self.children:
            s += node.to_html()
        s += f"</{self.tag}>"
        return s
    
