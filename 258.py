class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            v = 0
            while num>0:
                v += num%10
                num //= 10
            num = v
        
        return num
      
# 這題一直相加每個位數，直到變成單位數
# 第一個做法就是暴力解，一直更新原始的數字做計算
# 第二種做法可以看 solution(free)
