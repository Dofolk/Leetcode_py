class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n != 1:
            if not n%5:
                n //= 5
            elif not n%3:
                n //= 3
            elif not n%2:
                n //= 2
            else:
                return False
        return True
   
# 判斷放進來的數字有沒有2,3,5以外的質因數
# 所以這邊就是先判斷<=0。因為這些都不會有這些因數
# 然後就開始判斷有沒有235的因數，有的話就可以整除，所以就看有沒有整除來判斷
