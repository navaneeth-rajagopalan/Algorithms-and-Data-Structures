import enum

class TreeTraversalOrder(enum.Enum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3


class TreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree():

    def __init__(self):
        self.root = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.getSize() == 0

    def add(self, value):
        if self.isEmpty():
            self.root = self.TreeNode(value)
            self.size += 1
            return
        trav = self.root
        self._add(trav, value)
        self.size += 1

    def _add(self, trav, value):
        if value <= trav.value:
            if trav.left:
                self._add(trav.left, value)
            else:
                trav.left = self.TreeNode(value)
                return
        else:
            if trav.right:
                self._add(trav.right, value)
            else:
                trav.right = self.TreeNode(value)
                return
    
    def contains(self, value):
        if self.isEmpty():
            return False
        trav = self.root
        return self._contains(trav, value)

    def _contains(self, trav, value):
        if trav == None:
            return False
        if trav.value == value:
            return True
        if value <= trav.value:
            return self._contains(trav.left, value)
        else:
            return self._contains(trav.right, value)

    def traverse(self, order):
        trav = self.root
        ordered_nodes = []
        if order == TreeTraversalOrder.IN_ORDER:
            self._inOrderTraversal(trav, ordered_nodes)
        elif order == TreeTraversalOrder.PRE_ORDER:
            self._preOrderTraversal(trav, ordered_nodes)
        elif order == TreeTraversalOrder.POST_ORDER:
            self._postOrderTraversal(trav, ordered_nodes)
        return ordered_nodes

    def _inOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        self._inOrderTraversal(trav.left, ordered_nodes)
        ordered_nodes.append(trav.value)
        self._inOrderTraversal(trav.right, ordered_nodes)
    
    def _preOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        ordered_nodes.append(trav.value)
        self._preOrderTraversal(trav.left, ordered_nodes)        
        self._preOrderTraversal(trav.right, ordered_nodes)
    
    def _postOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        self._postOrderTraversal(trav.left, ordered_nodes)        
        self._postOrderTraversal(trav.right, ordered_nodes)
        ordered_nodes.append(trav.value)