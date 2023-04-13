# 這題是一個範圍指定說兩個人在玩的時候總共有那些數字可以用以及一個目標數字，然後看看能不能贏
# 想法是用 mask
# TBC

class Solution:
    def canIWin(self, M : int, T : int) -> bool:
        # M = maxChoosableInteger, T = desiredTotal
        if (M+1) * M // 2 < T:
            return False
        
        @cache
        def dfs(total, mask):
            win = False
            for i in range(M):
                if mask >> i & 1 == 0:
                    val = total + i + 1
                    if val >= T:
                        win = True
                        break
                    newMask = mask | 1 << i
                    if not dfs(val, newMask):
                        win = True
                        break
            return win
        
        return dfs(0, 0)
