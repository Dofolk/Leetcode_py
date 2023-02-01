# 這題給一個數字，然後把它變成相加的狀況，把相加數全部乘起來，找最大的是多少
# 做法就是用 Dynamic Programming，然後每個數字都變成a+b的形式，然後分別去找小數字的相乘就可以了

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for m in range(2, n + 1):
            i, j = 1, m - 1
            M = 0
            while i <= j:
                M = max( M, max(i, dp[i]) * max(j, dp[j]) )
                i += 1
                j -= 1
            dp.append(M)
        return dp[n]
