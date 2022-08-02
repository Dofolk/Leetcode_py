# 這題要找快樂數
# 第一種作法就是一直循環做各個位數的平方和，暴力法解決問題，基本上最外圈的while應該是不會超過50次
# 第二種做法就是把算過的植存起來，因為非快樂數的到最後會有幾個數字一直重複輪迴，再加上算到最後是1的時候不管怎樣後面一定永遠是1
# 根據這些特性，把算過的值存起來就可以檢測有沒有要跳出while，最後判斷要回傳 ture or false

class Solution:

# Solution 1
    def isHappy(self, n: int) -> bool:
        T = [4,16,20,37,42,58,89,145]
        i = 0
        while i<50:
            v = 0
            while n:
                v += (n%10)**2
                n //= 10
            if v in T:
                return False
            elif v == 1:
                return True
            else:
                n = v
        return False

# Solution 2
    def isHappy(self, n: int) -> bool:
        T = []
        while n not in T:
            T.append(n)
            n = sum([int(x)**2 for x in str(n)])
        return True if n==1 else False
