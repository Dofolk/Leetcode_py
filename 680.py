# 這題是要看在最多可以移除一個字元的狀況下，字串有沒有對稱
# 做法就跟之前做對稱的一樣，只是在第一次遇到有對不上的時候直接跳過有問題的那個位置並且回傳跳過之後的比對結果
# 因為比對的時候不確定是靠前面的位置錯了還是靠後面的，所以就是都找一遍並用 or 來取結果

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isP(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isP(s, i + 1, j) or isP(s, i, j - 1)
            i += 1
            j -= 1
        return True
