

def parse_tuple(structure, parent=None):
    if parent is None:
        parent = Node(parent)       
    for substructure in structure:
        child = parent.add_child()
        parse_tuple(substructure, child)
    return parent

        
class Node:
    
    def __init__(self, parent):
        self.parent = parent
        self.children = list()
        self.direct_children = 0
        
    def add_child(self):
        child = Node(self)
        self.children.append(child)
        self.direct_children += 1
        return child
    
    def num_children(self):
        if self.direct_children == 0:
            return 0
        else:
            return self.direct_children + sum([child.num_children() for child in self.children])
        
    def __getitem__(self, index: int):
        return self.children[index]
    
    def __repr__(self):
        if len(self.children) == 0:
            return "()"
        else:
            return "(" + "".join(str(child) for child in self.children) + ")"
        
        

class Tree:
    
    def __init__(self, root):
        self.root = root
        
    @classmethod
    def from_structure(cls, structure: tuple[int]):
        return cls(parse_tuple(structure))
        

