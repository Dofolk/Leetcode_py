# 這題是給一個數字唯一的 list，美個數字不能重複使用，找有幾組四數組合可以第1,2個數字相乘=第3,4個數字相乘
# 先想一下題目的數組，其實是有點排列順序的問題，所以就是找到有兩兩數字組合可以一樣就對了
# 這樣的話就是直接 double for 來看看所以相乘的結果出現幾次
# 然後依照出現的次數算 n*(n-1) /2 來記錄次數(C n 取 2)
# 最後回傳計算出線的8倍就好(排列組合的數量)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        L = len(nums)
        if len(nums) < 4:
            return 0
        pairs_count = dict()
        for idx, numa in enumerate(nums):
            for numb in nums[idx+1:]:
                prod = numa * numb
                if prod in pairs_count:
                    pairs_count[prod] += 1
                else:
                    pairs_count[prod] = 1
        ans = 0
        for prod, count in pairs_count.items():
            if count > 1:
                ans += count*(count - 1)//2
        return 8 * ans
