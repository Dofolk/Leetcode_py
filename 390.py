# 這題是給一個遞增的連續 n list (1,2,...,n) 裡面，先由左而右間隔移除值(1,3,5,...)，然後再從右邊開始移除(一樣的作法)，找最後剩下的數字是多少
# 觀察一下可以知道第一步會把 135 的奇數移除掉，所以剩下 246 = 2 * 123，所以這邊就變成 2 倍的下一個操作

class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        return 2 * ( n // 2 - self.lastRemaining(n // 2) + 1 )
