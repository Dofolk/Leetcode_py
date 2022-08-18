# 這題給定一個數字，然後看能疊出多高的樓梯
# 方法有幾種，樓梯高度(k)與所需的數量(S)關係為 S = k*(k+1)/2
# 第一個方法暴力解，就真的一個一個去算
# 第二個方法就是 binary search，對區間做 contraction
# 第三個方法就是先計算 S ，得到 k <= sqrt( 2S-1/4 )+1/2

class Solution:
  
# Solution 1
    def arrangeCoins(self, n: int) -> int:
        v = 0
        for i in range(n):
            v += i
            if v > n:
                return i-1
            elif v == n:
                return i
              
# Solution 2
    def arrangeCoins(self, n: int) -> int:
        a, b = 0, 65536
        while a <= b:
            p = (a+b) // 2
            v = p * (p+1) // 2
            if v == n:
                return p
            if v > n:
                b = p - 1
            else:
                a = p + 1
        return b
  
# Solution 3
    def arrangeCoins(self, n: int) -> int:
        return int((2*n+0.25)**0.5-0.5)
