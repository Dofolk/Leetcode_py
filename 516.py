# 這題是要找回最長的文子序列
# 做法就是用 DP 的做法下去做，從最尾端開始來做加總，最後一個字->最後2個字->...->第一個字
# 這樣慢慢的增加數量逐步疊上來

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(n-1, -1, -1):
            L = 0
            for j in range(i+1, n, 1):
                val = dp[j]
                if s[i] == s[j]:
                    dp[j] = L + 2
                L = max(L, val)
        
        return max(dp)
        
