# ===== Question =====
# 有一堆共 n 顆石頭，Alice 和 Bob 輪流拿，Alice 先手，第一回合必須拿 10 顆。
# 之後每回合都必須比上一回合少拿 1 顆，所以 Bob 拿 9 顆、Alice 拿 8 顆，依此類推。
# 輪到誰時，如果剩下的石頭不夠拿，誰就輸；若 Alice 獲勝，回傳 True，否則回傳 False。

# ===== Thoughts =====
# 這題直接做模擬，每一輪直接去做過一遍就可以了
# 這邊偶數就是 Bob 會贏

# Method - Enumeration
class Solution:
    def canAliceWin(self, n: int) -> bool:
        for turn in range(10, -1, -1):
            if n < turn:
                return bool(turn & 1)
            n -= turn
        return False
