# 這題是給一個字串跟數字 k，然後找看看子字串裡面有每個字母都連續出現大於等於 k 次的最長字串是多長
# 做法就是用 set 來看目前有哪些字母，然後去看看數量有沒有超過，沒超過直接下面一位，有超過的話就 split() 去湊其他字串出來

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max( self.longestSubstring(t,k) for t in s.split(c))
        return len(s)
