# 這題是給一串數字，然後去計算最大的值是多少，其計算方式是 0*idx0 + 1*idx1 + ...，然後idx可以做rotation
# https://leetcode.com/problems/rotate-function/solutions/195613/6-lines-python-o-n-time-o-1-space-with-explanation/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res = cur = sum( i*j for i,j in enumerate(nums) )
        L = len(nums)
        S = sum(nums)

        while nums:
            cur += S - L * nums.pop()
            res = max(res, cur)
        
        return res
