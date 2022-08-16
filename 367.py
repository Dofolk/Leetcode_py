# 這題是不用 sqrt 來確認是不是完全平方數
# 第一個做法就是確認長度，然後計算對半切的數字就好
# 第二個做法是用 binary search，一樣對半切然後收縮到一個值


class Solution:
  
# Solution 1
    def isPerfectSquare(self, num: int) -> bool:
        L = len(str(num))
        if L%2:
            L += 1
        i = 1
        while 1:
            v = i*i
            if v == num:
                return True
            elif v > num or i > pow(10,L//2):
                return False
            i += 1
            
# Solution 2
    def isPerfectSquare(self, num: int) -> bool:
        s = 0
        e = num
        while s<=e:
            v = (s+e)//2
            if v*v == num:
                return True
            elif v*v > num:
                e = v - 1
            else:
                s = v + 1
        return False
