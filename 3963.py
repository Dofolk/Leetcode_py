# ===== Question =====
# 題目會給 m, n 兩個常數，然後要回傳 m 個長度為 n 的字串
# 字串包含兩個字元: '.' 代表空格, '#' 代表障礙
# 假設把這些 m 個字串排起來看成是二維陣列，回傳一個陣列
# 然後該陣列只有一條從左上到右下的 path

# ===== Thoughts =====
# 這題就是直接生一個陣列出來就好，對簡單的就是先往左走到底之後再往下走到終點就好
# 要其他的方式也是可以，反正只要往左往下(只能左跟下)，直接走一條路到終點就好

# Method - Directly run
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        res.append('.' * n)
        for _ in range(m - 1):
            res.append('#' * (n - 1) + '.')
        return res
