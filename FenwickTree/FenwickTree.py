class FenwickTree:

    def __init__(self, nums):
        self.nums = nums
        self.bin_idx_tree = self.construct(nums)
        self.size = len(nums)
    
    def lsb(self, idx):
        if idx == 0: return 0
        lsb_off = idx & (idx - 1)
        return idx - lsb_off

    def construct(self, nums):
        bin_idx_tree = nums.copy()
        bin_idx_tree.insert(0, 0)
        N = len(bin_idx_tree)
        for idx in range(1, N):
            resp_idx = idx + self.lsb(idx)
            if resp_idx < N:
                bin_idx_tree[resp_idx] = bin_idx_tree[resp_idx] + bin_idx_tree[idx]
        return bin_idx_tree
    
    def sum(self, idx):
        idx += 1
        sum_val = 0
        while idx > 0:
            sum_val += self.bin_idx_tree[idx]
            idx -= self.lsb(idx)
        return sum_val

    def query(self, left_idx, right_idx):
        if left_idx > right_idx:
            raise Exception("Left index must be <= right index")
        if left_idx < 0 or right_idx >= self.size:
            raise Exception("Index out of range")
        if right_idx > left_idx:
            return self.sum(right_idx) - self.sum(left_idx - 1)
        else:
            return self.sum(right_idx) - self.sum(right_idx - 1)
    
    def update(self, idx, new_val):
        if 0 <= idx < self.size:
            delta = new_val - self.nums[idx]
            self.nums[idx] = new_val
            idx += 1
            while idx <= self.size:
                self.bin_idx_tree[idx] += delta
                idx += self.lsb(idx)
        else:
            raise Exception("Index out of range")
