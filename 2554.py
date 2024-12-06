# 這題是給一個 list 代表該數字被 ban 掉，然後再給一個數字 n 及上限 maxSum，現在從區間 [1,n] 之間選數字出來，最多可以選幾個數字不超過上限，也不選取被 ban 掉的數字
# 想法就是蠻簡單的，先把 ban 的數字變成 set 來加速搜尋的效率，然後從頭從最小的數字開始加，這樣可以算到最多個數字
# 然後就可以按照順序，先確認有沒有被 ban 掉，然後再確認當下的數字加上去會不會爆掉，爆掉就回傳目前有遇到幾個數字，沒有爆掉就加上去並增加遇到的數字數量

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        Sum, Num = 0, 0
        for i in range(1, n + 1):
            if i not in banned:
                if Sum + i > maxSum:
                    return Num
                Sum += i
                Num += 1
        return Num
