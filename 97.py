# 這題是要找看看兩個字串能不能合成第三個字串
# 想法就是做出一個二維陣列，代表著能走跟不能走的路徑
  # 然後做一個雙重回圈，把 s1 的每個字母當成起點，然後往後走 s2 的字母，或是找看看s1的字母能在哪邊被放入並且路還要能走
# 也可以就是用 DFS 下去做，想法就也是二維陣列，只是變成是把二維陣列的座標放進去走過的 set 裡面，表示這個點是走不可以走的
# 這題有公開解答

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:    
        memo = {}
        def dfs(i, j):
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i + j == len(s3):
                return True
            
            memo[(i, j)] = False
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                memo[(i, j)] = True
                return True
                    
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                memo[(i, j)] = True
                return True

            return memo[(i, j)]
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        return dfs(0, 0)
     
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, m = len(s1), len(s2)
        if M+m != len(s3): return False
        if M < m:
            M, m = m, M
            s1, s2 = s2, s1
        dp = [True] + [False]*m
        for i in range(1,m+1):
            dp[i] = s2[i-1]==s3[i-1] and dp[i-1]
        for i in range(1,M+1):
            dp[0] = s1[i-1]==s3[i-1] and dp[0]
            for j in range(1,m+1):
                dp[j] = s1[i-1]==s3[i+j-1] and dp[j]
                dp[j] = dp[j] or (s2[j-1]==s3[i+j-1] and dp[j-1])
        return dp[-1]
