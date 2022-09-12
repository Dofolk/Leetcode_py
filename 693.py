# 這題是要看一個數字的二進位表是法有沒有交替的位元 (就是 1 跟 0 相交)
# 做法就是先轉成二進制，然後逐個做比對就完事了

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = format(n,'b')
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                return False
        return True
