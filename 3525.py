# ===== Question =====
# 題目給一個正整數列表 nums 跟一個正整數 k，以及一個 queries: [index, value, start, x]，然後要回傳一個長度為 query 的結果 res
# 每個 query 會做得事情是先把 nums[idx] 的數值改成 value，再把 nums[0, start - 1] 這個區間段的數字忽略不計
# 然後剩下的區間段 nums[start, end] 可以做 suffix 的移除來獲得 sub array
# 這些 sub array 的總乘積 mod k 之後的餘數剛好等於 x 的數量全部有幾個

# ===== Thoughts =====
# 這題可以用 Segment Tree 來做動態的區間段更新及sub array 數量的 query
# Segment Tree 這邊的每個 node 就會持續記錄兩個資訊: nums[idx] 的數值以及相對應餘數的 count 紀錄
# 現在每做一個 query，就會先去 update Segment Tree 的點資訊，更新完畢之後再去 query 結果
# 最後把結果記錄起來回傳就可以了

# Method - Segment Tree
class SegmentTree:
    def __init__(self, a: List[int], k: int):
        self._n = n = len(a)
        self._k = k
        self._tree = [None] * (2 << (n - 1).bit_length())
        self._build(a, 1, 0, n - 1)

    # Merge the current status of two sub node to the parent node
    def _merge(self, a: Tuple[int, List[int]], b: Tuple[int, List[int]]) -> Tuple[int, List[int]]:
        counts = a[1].copy()
        left_multi = a[0]
        for idx, count in enumerate(b[1]):
            counts[left_multi * idx % self._k] += count
        return left_multi * b[0] % self._k, counts
    
    # Here comes new data for leaf node
    def _new_data(self, val: int) -> Tuple[int, List[int]]:
        multi = val % self._k
        counts = [0] * self._k
        counts[multi] = 1
        return multi, counts
    
    # Merge left/right child info in current node
    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge(self._tree[node * 2], self._tree[node * 2 + 1])
    
    # Build up the segment tree with first time initialize the tree
    def _build(self, a: List[int], node: int, left: int, right: int) -> None:
        if left == right: # Leaf node
            self._tree[node] = self._new_data(a[left])
            return
        mid = (left + right) // 2
        self._build(a, node * 2, left, mid)
        self._build(a, node * 2 + 1, mid + 1, right)
        self._maintain(node)

    # Update the the tree node when there is new data or new modification
    def _update(self, node: int, left: int, right: int, idx: int, val: int) -> None:
        if left == right: # Leaf node
            self._tree[node] = self._new_data(val)
            return
        mid = (left + right) // 2
        if idx <= mid: # index at left sub tree
            self._update(node * 2, left, mid, idx, val)
        else: # index at right sub tree
            self._update(node * 2 + 1, mid + 1, right, idx, val)
        
        self._maintain(node)
    
    # Query the target interval [query_left, query_right] in interval [left, right] 
    def _query(self, node: int, left: int, right: int, query_left: int, query_right: int) -> Tuple[int, List[int]]:
        # Query range is fully cover the current interval [left, right]
        if query_left <= left and right <= query_right:
            return self._tree[node]
        mid = (left + right) // 2
        # Query range is fully under left sub tree
        if query_right <= mid:
            return self._query(node * 2, left, mid, query_left, query_right)
        # Query range is fully under right sub tree
        if query_left > mid:
            return self._query(node * 2 + 1, mid + 1, right, query_left, query_right)
        left_res = self._query(node * 2, left, mid, query_left, query_right)
        right_res = self._query(node * 2 + 1, mid + 1, right, query_left, query_right)
        return self._merge(left_res, right_res)
    
    # Update tree[idx] with _new_data(val)
    # Time Complexity: O(log n)
    def update(self, idx: int, val: int) -> None:
        self._update(1, 0, self._n - 1, idx, val)
    
    # Return the result from _merge() which merge up all result of tree[idx] where idx in [query_left, query_right] 
    # Time Complexity: O(log n)
    def query(self, query_left: int, query_right: int) -> Tuple[int, List[int]]:
        return self._query(1, 0, self._n - 1, query_left, query_right)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums, k)
        n = len(nums)
        ans = []

        for idx, val, start, x in queries:
            tree.update(idx, val)
            _, count = tree.query(start, n - 1)
            ans.append(count[x])
        
        return ans
