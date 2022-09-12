# 這題是給一串字元，然後計算出最終的分數
# 遇到 C 就移除前一個數字，D 就前一個數字加倍後留著，+ 就前兩個相加後留著
# 做法就是直接操作，用一個 res 來存操作的東西，用 if elif 判斷並做出相對應的操作

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == "C": res.pop()
            elif i == "D": res.append(res[-1]*2)
            elif i == "+": res.append(res[-1]+res[-2])
            else: res.append(int(i))
        return sum(res)
