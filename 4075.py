# ===== Question =====
# 題目會給一個數字 n 代表數字上限還有一個數字 s 代表總和目標值
# 然後要從 <= n 的所有質數(每個質數只能選一次)組一個 list 出來然後總和要 <= 目標
# 這邊答案可以有很多個回傳任一個就可以了
# 像是 7 的狀況可以回傳 2+5或2+3都可以

# ===== Thoughts =====
# 這題的限制非常的寬鬆所以可以先用埃拉托斯特尼篩法找出所有 ≤ n 的質數
# 然後再從小的質數開始累積並儲存遇到的質數，超過目標或是 n 的時候再回傳值就好了

# Method 1 - Directly Check
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        v1, v2, v3 = 0, 1, 1
        curr = 2
        for _ in range(n):
            if curr == n:
                return True
            elif curr > n:
                return False
            curr -= v1
            v1, v2, v3 = v2, v3, v2 + v3
            curr += v3

        return False
