# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a, b = 1, n
        while a<b:
            p = (a+b)//2
            if isBadVersion(p):
                b = p
            else:
                a = p + 1
        
        return a
      
# 這題是要找最開始有問題的值是哪個值
# 所以就用 binary 來做，一半一半切
