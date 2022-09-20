# 這題是要做數字的反轉，並且確認不會超出界線 2^31
# 作法就是直接做，先把數字變成字串然後作反轉，再看看有沒有超過界線就好

class Solution:
    def reverse(self, x: int) -> int:
        if '-' in str(x):
            s = str(x)[::-1]
            if int('-'+s[0:-1])> -2**31:
                return int('-'+s[0:-1])
            else:
                return 0
        else:
            if int(str(x)[::-1])< (2**31-1):
                return int(str(x)[::-1])
            else:
                return 0
