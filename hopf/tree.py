from copy import deepcopy


def to_tuple(parens):
    """
    """
    if parens == []:
        return ()
    else:
        return tuple([to_tuple(inner) for inner in parens])
    

def to_list(parens):
    if parens == ():
        return []
    else:
        return [to_list(inner) for inner in parens]
    


class Tree:

    """
    """
    
    def __init__(self, structure, parent):
        self.parent = parent
        self.structure = to_tuple(structure)
        self.children = [
            Tree(sub, self) for  sub in structure
        ]
    
    @property
    def num_children(self):
        if self.direct_children == 0:
            return 0
        else:
            return (
                self.direct_children 
                + sum([child.num_children for child in self.children])
            )
    
    def cut(self, index: int) -> tuple:
        branch = Tree(self.children[index].structure, None)
        cut_structure = deepcopy(self.structure)
        cut_structure.pop(index)
        root = Tree(cut_structure, deepcopy(self.parent), self.value)
        return root, branch

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.children[index]
        elif isinstance(index, tuple):
            node = self
            for i in index:
                node = node[i]
            return node
        else:
            raise NotImplementedError

    def __repr__(self):
        if len(self.children) == 0:
            return "()"
        else:
            return (
                "("
                + "".join(str(child) for child in self.children) 
                + ")"
            )
        
    def __hash__(self):
        return hash(str(self))
