# 這題就是轉成7進位制，做法就是簡單的while迴圈跑完就可以了
# 然後在負號的部分就是考慮數字就可以了，負號最後再加就行了( -1 = -1, -7 = -10, -8 = -11)

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        neg = 0
        if num < 0:
            neg = 1
        num = abs(num)
        ls = list()
        while num:
            ls.append(str(num%7))
            num //= 7
        if neg:
            ls.append('-')
        
        s = ''.join(ls[::-1])
        return s
        
