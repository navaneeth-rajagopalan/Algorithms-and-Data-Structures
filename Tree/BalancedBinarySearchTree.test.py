from BalancedBinarySearchTree import BalancedBinarySearchTree, TreeTraversalOrder

from random import randint, random

Tests = 10
while Tests > 0:
    size = randint(5, 50)
    nums = []
    for i in range(size):
        nums.append(randint(-50, 50))

    bbTree = BalancedBinarySearchTree()

    for num in nums:
        bbTree.insert(num)
        
    print("===== Level Order Traversal Results =====")
    ordered_tree = bbTree.traverse(TreeTraversalOrder.LEVEL_ORDER)
    print(ordered_tree)
    
    ordered_tree = bbTree.traverse(TreeTraversalOrder.IN_ORDER)
    
    assert ordered_tree == sorted( list( set(nums) ) )
    
   
    Tests -= 1
print("All test cases passed!")