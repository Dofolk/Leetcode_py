# 這題是給兩個字串，然後操作的方法有三種：換字、加字跟移除，目標是找出最少操作的次數
# 把兩個字做成矩陣的形式，然後先把行列各為 0 的先處理好(如果其中一個是空字串就是最簡單的全部操作都做新增)
# 接下來逐個把字加回來，去看看當下的情況字有沒有一樣，一樣的話就是都不用動，把前面的結果拿來用
# 不一樣的話就是需要做一次操作(換字之類的)，所以就把前面有可能出現的狀況找最小的出來加一步操作


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [ [0] * (n + 1) for _ in range(m + 1) ]

        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min( dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1] ) + 1
        
        return dp[m][n]
