from FenwickTree import FenwickTree
from random import randint, random

size = randint(0, 1000)
nums = []
for i in range(size):
    nums.append(randint(-500, 500))

fenTree = FenwickTree(nums)

T = 200

while T > 0:
    do_update = random()
    if do_update < 0.25:
        update_idx = randint(0, size - 1)
        update_val = randint(-100, 100)
        fenTree.update(update_idx, update_val)

    left_index = randint(0, size - 1)
    right_index = randint(left_index, size - 1)
    fen_res = fenTree.query(left_index, right_index)
    test_res = sum(nums[left_index: right_index + 1])

    assert fen_res == test_res

    T -= 1
print("All test cases passed!")