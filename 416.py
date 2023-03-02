# 這題會給一個數字列表，然後把它分成兩個表，看能不能讓兩個表總和一樣
# 這題就是 0/1 背包問題(knapback problem)，可以看演算法筆記，有詳細的說明

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S, L = sum(nums), len(nums)
        if S & 1:
            return False
        
        target = S//2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[target]:
                    return True
                dp[i] = dp[i] or dp[i - num]
        return dp[target]
