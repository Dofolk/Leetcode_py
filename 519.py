# 這題是給一個 m x n 的零矩陣，然後隨機對其中一個位置改變數值變成1
# 目標是要設計一個能夠創建、修改數值跟重製的方法，然後對於每個位置都平均一樣的機率取樣到
# 做法就是用一個 set 來記錄使用過的位置，然後下次隨機選後就檢查有沒有用過，用過就下面一位繼續找
# 這樣的 reset 方法很簡單，直接給一個空 set 就好
# 另解也有 fisher yates shuffle 方法，但先 pass

class Solution:

    def __init__(self, m: int, n: int):
        self.used = set()
        self.total = m*n
        self.m = m
        self.n = n
        self.r = random.Random()

    def flip(self) -> List[int]:
        val = self.r.randint(0, self.total - 1)
        while val in self.used:
            val = self.r.randint(0, self.total - 1)
        self.used.add(val)
        return [val // self.n, val % self.n]
        
    def reset(self) -> None:
        self.used = set()
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
