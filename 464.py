# 這題是一個範圍指定說兩個人在玩的時候總共有那些數字可以用以及一個目標數字，然後看看能不能贏
# 想法是用 mask 來記錄目前使用過的數字有哪些(舉例來說 10101 代表說 135 這 3 個數字被使用過)
# 然後判斷一下目前的total加上所選擇的數字(i+1, 因為index從0開始)有沒有比目標還大，有的話就代表說可以贏，沒有的話就下一輪判斷
# 下一輪的判斷就是說去看看另一個人會不會贏不了，因為當下一輪判斷是會贏的話你就輸定了(因為會一直遞回下去找完所有的可能性，並依照後面的判斷來給回覆)
# 但下一輪判斷輸的話就是代表對手不管怎樣都沒招了，代表說自己可以贏
# 最後就回傳從 0, 0 開始跑一輪的結果
# 這邊會設定 @cache 來記錄走過的組合，因為運算量太大，避免重複運算炸電腦

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
