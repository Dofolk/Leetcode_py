# 這題是要找 n 階層會有多少個 0 在尾巴
# 做法就是去算有幾個 5，算法就是看 n 能被 5 整除？接下來就是能被 25 整除？....一直到超過 n 為止

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cur = 5
        res = 0
        while cur <= n:
            res += n//cur
            cur *= 5
        return res
