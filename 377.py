# 這題是要給定目標值跟數字表，能有多少組合
# 做法就是 DP，從小疊加到大，0的時候就是0，1的時候就是看看有沒有1+0，2就是往前去加1跟0的(因為可以去組合出來)
# 所以就是for跑一遍就可以了

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for Sum in range(1, target + 1):
            for n in nums:
                if Sum - n >= 0:
                    dp[Sum] += dp[Sum - n]
                else:
                    break
        
        return dp[target]
