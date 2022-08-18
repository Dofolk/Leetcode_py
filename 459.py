# 這題是要找出自串中有沒有重複一直出現的子字串
# 第一個方法是 KMP algorithm，把原本的字串拿來做比對，找看看最長的子字串是多長，再去判斷沒有沒重複
# 第二個方法就比較簡單暴力，直接字串兩倍化後頭尾相接並去掉頭尾，然後看看原始字串有沒有在裡面

class Solution:
  
# Solution 1
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j

        l = dp[n - 1]
        return l != 0 and n % (n - l) == 0
      
# Solution 2
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
