# 這題是檢測看看數字是不是 3 的高次方數
# <=0 的數字一定都是不對的，可以先排除掉
# 剩下就用 while 來看看除3之後有沒有餘數

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n%3:
                return False
            n //= 3
        
        return True
