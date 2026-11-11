# ===== Question =====
# 你從第 0 階出發，要到達第 n 階，每次只能往上跳 1、2 或 3 階。
# 每次跳躍的花費是「落點階梯的費用＋跳躍階數的平方」。
# 回傳到達第 n 階所需的最小總花費。

# ===== Thoughts =====
# 這題就是典型的 DP，每一次都去更新往前三步之內走到當下位置的話會需要多少 cost
# 然後題目就是往前三步之後的資訊，所以其實可以簡化成 3 項的 sliding window

# Method 1 - Sliding Window Like
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        step1, step2, step3 = 0, 0, 0

        for cost in costs:
            step1, step2, step3 = step2, step3, min(step1 + 9, step2 + 4, step3 + 1) + cost
        
        return step3

# Method 2 - DP
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        costs = [0] + costs

        for idx in range(1, n + 1):
            # one step
            m = dp[idx - 1] + 1

            # two steps
            if idx - 2 >= 0:
                m = min(m, dp[idx - 2] + 4)
            
            # three steps
            if idx - 3 >= 0:
                m = min(m, dp[idx - 3] + 9)
            
            dp[idx] = m + costs[idx]
        
        return dp[-1]
