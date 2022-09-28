# 這題是要找 x^n，然後沒說不能用 pow 等內建的函式
# 所以直接call就可以了
# 或是把自己當成其他語言，用遞迴式來做，遇到次方數為 1 時就回傳值，然後找出對半 n 的值(x^(n/2))，然後依據奇偶作乘法回傳就可以了

class Solution:
# 1
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)
# 2
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            x = 1/x
            n = -n
        def power(x,n):
            if n == 1:
                return x
            half = power(x,n//2)
            if n%2:
                return half*half*x
            else:
                return half*half
        
        return power(x,n)
        
