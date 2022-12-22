# 這題是要找 list 裡面第 K 大的值是多少，然後要在 O(N) 內完成
# 直接sort

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
