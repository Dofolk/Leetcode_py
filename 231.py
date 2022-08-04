# 這題是要看這個數字是不是 2 的 N 次方數
# 兩個做法都先把 >=0 排除，因為 2^N >=1
# 作法就是一直除 2 看有沒有餘數 1 出現

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n >= 1:
            if n == 1:
                return True
            if n%2 == 1:
                return False
            n //= 2
