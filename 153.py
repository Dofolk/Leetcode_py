# 這題是給一個遞增陣列，然後他會 rotate，其實就跟 33 題很像，可能會有一段後面的遞增子序列拉到前面去，最後要找 min
# 最簡單作法直接回傳 min(nums)
# 不然就是 binary search，找中間點跟最右邊比，比較大的話代表後段遞增數列比較長，所以左邊點往中間靠，反之就是右邊往中間靠

class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        while L < R:
            m = (L+R)//2
            if nums[m] < nums[R]:
                R = m
            else:
                L = m + 1
        return nums[L]
