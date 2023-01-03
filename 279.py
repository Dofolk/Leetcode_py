# 這題是給一個值，然後找看看最少可以用幾個平方數加起來會相等
# 這題跟所謂得四平方核定理有關
# 可以參考https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
# 或https://www.cnblogs.com/grandyang/p/4800552.html


from math import isqrt

class Solution:
    def numSquares(self , n):
        
        if isqrt(n)**2 == n : return 1               
        
        for i in range(1,isqrt(n)+1):
            if (j := n - i**2) == isqrt(j)**2:
                return 2
            
        while n % 4 == 0 : n /= 4
        if    n % 8 != 7 : return 3
        
        return 4        
