import BinarySearchTree

my_bst = BinarySearchTree.Tree()
my_bst.add(11)
my_bst.add(6)
my_bst.add(8)
my_bst.add(3)
my_bst.add(15)
my_bst.add(13)
my_bst.add(17)
my_bst.add(19)
my_bst.add(14)
my_bst.add(12)
my_bst.add(3)
my_bst.add(1)
my_bst.add(5)

ordered_tree = my_bst.traverse(BinarySearchTree.TreeTraversalOrder.IN_ORDER)
print(ordered_tree)
print("\n\n")
ordered_tree = my_bst.traverse(BinarySearchTree.TreeTraversalOrder.PRE_ORDER)
print(ordered_tree)
print("\n\n")
ordered_tree = my_bst.traverse(BinarySearchTree.TreeTraversalOrder.POST_ORDER)
print(ordered_tree)


my_alpha_bst = BinarySearchTree.Tree()
my_alpha_bst.add('A')
my_alpha_bst.add('B')
my_alpha_bst.add('C')
my_alpha_bst.add('D')
my_alpha_bst.add('F')
my_alpha_bst.add('K')
my_alpha_bst.add('G')
my_alpha_bst.add('L')
my_alpha_bst.add('J')
my_alpha_bst.add('I')
my_alpha_bst.add('H')
my_alpha_bst.add('E')

ordered_tree = my_alpha_bst.traverse(BinarySearchTree.TreeTraversalOrder.IN_ORDER)
print(ordered_tree)
print("\n\n")
ordered_tree = my_alpha_bst.traverse(BinarySearchTree.TreeTraversalOrder.PRE_ORDER)
print(ordered_tree)
print("\n\n")
ordered_tree = my_alpha_bst.traverse(BinarySearchTree.TreeTraversalOrder.POST_ORDER)
print(ordered_tree)