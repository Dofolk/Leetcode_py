# 這題是要找出多出來的字元是哪個
# 第一個做法就是把存在的元素都移除，剩下的東西就是多出來的那個字元了
# 第二個做法就是做 ascii 數字加總後找出差距的字元

class Solution:
  
# Solution 1
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        ls = list(t)
        for i in s:
            ls.remove(i)
        return ls[0]
      
# Solution 2
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = sum(ord(x) for x in s)
        s2 = sum(ord(y) for y in t)
        return chr(s2-s1)
