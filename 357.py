# 這題會給一個數字 n，然後從區間 [0,10^n) 裡面找出數字組合皆不重複的數字有幾個
# 做法就是往前加，一開始有10個，然後有 9 * 9 + 10 個( 9 * 9 是考慮十位數非 0 的狀況)，接著就考慮百位數非的狀況 0，一直下去

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def count(k):
            if k == max(10-n,0):
                return 0
            return k * ( 1 + count(k - 1) )
        if n == 0:
            return 1
        return 9 * count(9) + 10
