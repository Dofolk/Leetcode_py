# 這題是要找連續子序列總和最大是多少
# 想法是把第一個是數字當成最大，然後與下一個數字相加之後會不會比下一個數字大
# 會的話代表我往前加的值比較大，不會的話代表說我就直接取下一個數字就可以變成最大了，根本不需要前面那一串子序列

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
          nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)
