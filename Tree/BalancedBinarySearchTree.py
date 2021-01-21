import enum

class TreeTraversalOrder(enum.Enum):
    IN_ORDER = 1
    PRE_ORDER = 2
    POST_ORDER = 3
    LEVEL_ORDER = 4

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
        self.balance_factor = 0
    
    def __str__(self):
        return str(self.val)

class BalancedBinarySearchTree:

    def __init__(self):
        self.root = None
    
    def update(self, node):
        left_height, right_height = -1, -1
        if node.left: left_height = node.left.height
        if node.right: right_height = node.right.height
        node.height = 1 + max(left_height, right_height)
        node.balance_factor = right_height - left_height
    
    def left_rotate(self, node):
        node_right = node.right
        node.right = node_right.left
        node_right.left = node
        self.update(node)
        self.update(node_right)
        return node_right
    
    def right_rotate(self, node):
        node_left = node.left
        node.left = node_left.right
        node_left.right = node
        self.update(node)
        self.update(node_left)
        return node_left

    def left_left_case(self, node):
        # print("Left-Left-Case for {0}".format(node.val))
        rotated_node = self.right_rotate(node)
        # print("New root is {0} \t Left: {1} \t Right: {2}".format(rotated_node.val, rotated_node.left, rotated_node.right))
        return rotated_node
    
    def left_right_case(self, node):
        # print("Left-Right-Case for {0}".format(node.val))
        node.left = self.left_rotate(node.left)
        rotated_node = self.right_rotate(node)
        # print("New root is {0} \t Left: {1} \t Right: {2}".format(rotated_node.val, rotated_node.left, rotated_node.right))
        return rotated_node
    
    def right_right_case(self, node):
        # print("Right-Right-Case for {0}".format(node.val))
        rotated_node = self.left_rotate(node)
        # print("New root is {0} \t Left: {1} \t Right: {2}".format(rotated_node.val, rotated_node.left, rotated_node.right))
        return rotated_node
    
    def right_left_case(self, node):
        # print("Right-Left-Case for {0}".format(node.val))
        node.right = self.right_rotate(node.right)
        rotated_node = self.left_rotate(node)
        # print("New root is {0} \t Left: {1} \t Right: {2}".format(rotated_node.val, rotated_node.left, rotated_node.right))
        return rotated_node

    def balance(self, node):
        if node.balance_factor == -2:
            # Left heavy
            if node.left.balance_factor <= 0:
                # Left-Left heavy
                return self.left_left_case(node)
            else:
                # Left-Right heavy
                return self.left_right_case(node)
        elif node.balance_factor == 2:
            # Right heavy
            if node.right.balance_factor >= 0:
                # Right-Right heavy
                return self.right_right_case(node)
            else:
                # Right-Left heavy
                return self.right_left_case(node)
        else:
            # No need to balance
            return node

    def recurse_insert(self, node, val):
        if node == None:
            return Node(val)
        else:
            if val == node.val:
                return node
            elif val < node.val:
                node.left = self.recurse_insert(node.left, val)
            else:
                node.right = self.recurse_insert(node.right, val)
            self.update(node)
            return self.balance(node)

    def insert(self, val):
        self.root = self.recurse_insert(self.root, val)
    
    def traverse(self, order):
        trav = self.root
        ordered_nodes = []
        if order == TreeTraversalOrder.IN_ORDER:
            self._inOrderTraversal(trav, ordered_nodes)
        elif order == TreeTraversalOrder.PRE_ORDER:
            self._preOrderTraversal(trav, ordered_nodes)
        elif order == TreeTraversalOrder.POST_ORDER:
            self._postOrderTraversal(trav, ordered_nodes)
        elif order == TreeTraversalOrder.LEVEL_ORDER:
            self._levelOrderTraversal(trav, ordered_nodes)
        return ordered_nodes

    def _inOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        self._inOrderTraversal(trav.left, ordered_nodes)
        ordered_nodes.append(trav.val)
        self._inOrderTraversal(trav.right, ordered_nodes)
    
    def _preOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        ordered_nodes.append(trav.val)
        self._preOrderTraversal(trav.left, ordered_nodes)        
        self._preOrderTraversal(trav.right, ordered_nodes)
    
    def _postOrderTraversal(self, trav, ordered_nodes):
        if trav == None:
            return        
        self._postOrderTraversal(trav.left, ordered_nodes)        
        self._postOrderTraversal(trav.right, ordered_nodes)
        ordered_nodes.append(trav.val)

    def _levelOrderTraversal(self, trav, ordered_nodes):
        current = [trav]
        ptr = 0
        while ptr < len(current):
            node = current[ptr]
            if node:
                ordered_nodes.append(node.val)
                current.append(node.left)
                current.append(node.right)
            else:
                ordered_nodes.append("None")
            ptr += 1
