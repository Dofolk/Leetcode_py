# 這題是要算兩個數字的二進制的差異，每一個位元的差異是多少，也就是XOR的概念
# 第一個做法就是先把兩個數字變成二進，然後逐一檢查就可以了
# 第二跟三個作法就用到內建的 ^ (xor) 運算子來操作

class Solution:
  
# Solution 1
    def hammingDistance(self, x: int, y: int) -> int:
        v = 0
        s1 = format(x,'b').zfill(31)
        s2 = format(y,'b').zfill(31)
        for i in range(31):
            if s1[i] == '1' and s2[i] == '0':
                v += 1
            elif s1[i] == '0' and s2[i] == '1':
                v += 1
        return v
      
# Solution 2
    def hammingDistance(self, x: int, y: int) -> int:
        v = x^y
        s1 = format(v,'b')
        ans = 0
        for i in s1:
            if i == '1':
                ans += 1
        return ans
      
# Solution 3
    def hammingDistance(self, x: int, y: int) -> int:
        return format(x^y,'b').count('1')
