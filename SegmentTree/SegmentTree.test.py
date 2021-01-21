from SegmentTree import SegmentTree
from random import randint, random

Tests = 100
while Tests > 0:
    size = randint(0, 1000)
    nums = []
    for i in range(size):
        nums.append(randint(-500, 500))

    segTree = SegmentTree(nums)

    T = 1000
    while T > 0:
        do_update = random()
        if do_update < 0.25:
            update_idx = randint(0, size - 1)
            update_val = randint(-100, 100)
            segTree.update(update_idx, update_val)
        
        left_index = randint(0, size - 1)
        right_index = randint(left_index, size - 1)
        segTree_res = segTree.query(left_index, right_index)
        test_res = sum(nums[left_index: right_index + 1])

        assert segTree_res == test_res

        T -= 1
    Tests -= 1
print("All test cases passed!")