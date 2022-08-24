# 這題是要把某些特定段落的字串反轉，給定字串 s，常數 k，將 s 裡 (2nk~2nk+k) 的子字串反轉
# 做法就是直接做反轉，用 for+reversed() 操作就可以了

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0,len(s),2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)
