# 這題是從左上走到右下有多少種走法
# 就是一個排列組合問題，就照著 key 就好了，然後判斷一下 m,n 哪個比較大，用大的那個比較接近 m+n，可以少計算幾次

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        v1 = 1
        v2 = 1
        M = m if m>n else n
        for i in range(M+1,m+n+1):
            v1 *= i
            v2 *= (i-M)
        return int(v1/v2)
