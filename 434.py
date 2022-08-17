# 這題是要算字串以空格切開之後會剩下幾塊
# 第一個做法就是直接用 split()
# 第二個做法就是做前後確認，空白後一定要是非空白，這樣就會是一個可數的字串了，然後最一開始的時候就當成是空白的就行了
# 這樣才會算到最一開始的小字串

class Solution:
  
# Solution 1
    def countSegments(self, s: str) -> int:
        return len(s.split())
  
# Solution 2
    def countSegments(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                c += 1
        return c
