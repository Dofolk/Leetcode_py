# 這題是給一個整數 list，然後針對最靠前的最小值乘 multiplier，總共做 k 次，問最後整個 list 長怎樣
# 直接用 min() 跟 index() 找出目標，乘完之後就可以回傳了
# 這題因為整個限制很小，所以一般 list 就可以操作了，可以不用 heap，少了點建立 heap 的時間

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier
        return nums
