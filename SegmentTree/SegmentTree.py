class SegmentTree:

    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        self.seg_tree_size = len(nums)
        if self.seg_tree_size & (self.seg_tree_size - 1) != 0:
            self.seg_tree_size = self.seg_tree_size << 1
            while self.seg_tree_size & (self.seg_tree_size - 1) != 0:
                self.seg_tree_size &= (self.seg_tree_size - 1)
        self.seg_tree_size = self.seg_tree_size * 2 - 1
        self.seg_tree = [0 for i in range(self.seg_tree_size)]
        self.construct(nums, self.seg_tree, 0, 0, len(nums) - 1)
        
    def construct(self, nums, seg_tree, pos, left, right):
        if left == right:
            seg_tree[pos] = nums[left]
        else:
            mid = (left + right) // 2
            self.construct(nums, seg_tree, (pos * 2) + 1, left, mid)
            self.construct(nums, seg_tree, (pos * 2) + 2, mid + 1, right)
            seg_tree[pos] = seg_tree[(pos * 2) + 1] + seg_tree[(pos * 2) + 2]
    
    def deep_query(self, pos, pos_left_range, pos_right_range, query_left_idx, query_right_idx):
        # 1. Partial Overlap - recurse deeper
        # 2. Total Overlap - return value
        # 3. No Overlap - return 0
        if query_left_idx <= pos_left_range <= query_right_idx and \
            query_left_idx <= pos_right_range <= query_right_idx:
            # Total Overlap
            return self.seg_tree[pos]
        elif (pos_left_range < query_left_idx and pos_right_range < query_left_idx) or \
            (pos_left_range > query_right_idx and pos_right_range > query_right_idx):
            # No Overlap
            return 0
        else:
            # Partial Overlap
            mid = (pos_left_range + pos_right_range) // 2
            left_segment_val = \
                self.deep_query(pos * 2 + 1, pos_left_range, mid, query_left_idx, query_right_idx)
            right_segment_val = \
                self.deep_query(pos * 2 + 2, mid + 1, pos_right_range, query_left_idx, query_right_idx)
            return left_segment_val + right_segment_val
            

    def query(self, left_idx, right_idx):
        if left_idx > right_idx:
            raise Exception("Left index must be <= right index")
        if left_idx < 0 or right_idx >= self.size:
            raise Exception("Index out of range")
        return self.deep_query(0, 0, self.size - 1, left_idx, right_idx)
    
    def deep_update(self, pos, pos_left_range, pos_right_range, idx, delta):
        if pos_left_range == pos_right_range:
            if pos_left_range == idx:
                # Leaf positions
                self.seg_tree[pos] += delta
        elif pos_left_range <= idx <= pos_right_range:
            # the intermin node overlaps the index
            self.seg_tree[pos] += delta
            mid = (pos_left_range + pos_right_range) // 2
            self.deep_update(pos * 2 + 1, pos_left_range, mid, idx, delta)
            self.deep_update(pos * 2 + 2, mid + 1, pos_right_range, idx, delta)

    def update(self, idx, new_val):
        if 0 <= idx < self.size:
            delta = new_val - self.nums[idx]
            self.nums[idx] = new_val
            self.deep_update(0, 0, self.size - 1, idx, delta)
        else:
            raise Exception("Index out of range")