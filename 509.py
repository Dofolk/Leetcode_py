# 這題要找 Fabonacci Number
# 第一個做法就是暴力加
# 第二個就是用級數解得到數字 N = ( ( ( 1+sqrt(5) ) /2 )^n - ( ( 1-sqrt(5) ) /2 )^n ) / sqrt(5)

class Solution:
  
# Solution 1
    def fib(self, n: int) -> int:
        if n == 0: return 0
        n0, n1 = 0, 1
        for i in range(1,n):
            n0, n1 = n1, n0+n1
        
        return n1
     
# Solution 2
    def fib(self, n: int) -> int:
        alpha = (1-sqrt(5))/2
        beta = (1+sqrt(5))/2
        return int((pow(beta,n)-pow(alpha,n))/sqrt(5))
