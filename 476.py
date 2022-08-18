# 這題是要把數字的二進未做翻轉，01互換，然後回傳數字
# 第一個方法就是暴力解
# 第二個方法就是互補來想，既然翻轉的話就是找個一個數字跟 num+1 相加會等於某個 2^n，然後會往上一個位元，所以就找出 2^n > num，這確定好了相加的數字

class Solution:
  
#　Solution 1
    def findComplement(self, num: int) -> int:
        s = []
        for i in format(num,'b'):
            if i == '0':
                s.append('1')
            elif i == '1':
                s.append('0')
        return int(''.join(s),2)
      
# Solution 2
    def findComplement(self, num: int) -> int:
        i = 0
        while 2**i<=num:
            i+=1
        return 2**i-num-1
