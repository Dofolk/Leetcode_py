# 這題就是要把數字變成16進為表示法
# 然後負數也要做轉換， -1 就是 ffffffff， -2^31 就是 80000000

class Solution:
    def toHex(self, num: int) -> str:
        d = "0123456789abcedf"
        s = ''
        if num == 0:
            return "0"
        if num < 0:
            num += pow(2,32)
        
        while num:
            s += d[num%16]
            num //= 16
        
        return ''.join(s[::-1])
