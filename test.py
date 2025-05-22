class Node:
    def __init__(self, data, word):
        self.data = data
        self.word = word
        self.children = {}

    def add_child(self, child):
        self.children[child] = child

def tree_to_dict(node):
    if not node:
        return None
    
    tree_dict = {"data": node.data, "word": node.word}
    if node.children:
        tree_dict["children"] = {child.data: tree_to_dict(child) for child in node.children}
    return tree_dict

# Example Usage
root = Node(None,"A")
b = Node(2,"B")
c = Node(3,"C")
d = Node(4,"D")
e = Node(2,"E")
f = Node(1,"F")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

tree_dict = tree_to_dict(root)
print(tree_dict)

#
#class Tree(object):
#    "Generic tree node."
#    def __init__(self, name='root', children=None):
#        self.name = name
#        self.children = {}
#        if children is not None:
#            for child in children:
#                self.add_child(child)
#    def __repr__(self):
#        return self.name
#    def add_child(self, node):
#        assert isinstance(node, Tree)
#        self.children[node.name] = node
#
#tree = Tree()
#tree.add_child(Tree("a"))
#tree.add_child(Tree("b"))
#tree.add_child(Tree("c"))
#
#print(tree.children)
#
#tree.children["a"].add_child(Tree("aa"))
#tree.children["a"].add_child(Tree("ab"))
#
#print(tree.children)
#
