# 這題是給一個目標值跟數字列表，找看看總和是目標的最短 subarray 多長
# 做法就是用 two pointer，因為 subarray 的特性就是要連一起，所以就用類似 slide window 一樣逐漸增加數值或減少數值，直到符合目標或是到底

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = L = R = 0
        res = len(nums) + 1
        
        while R < len(nums):
            total += nums[R]
            while total >= target:
                res = min(res, R - L + 1)
                total -= nums[L]
                L += 1
            R += 1
        
        return res if res<=len(nums) else 0
