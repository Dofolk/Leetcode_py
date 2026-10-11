# ===== Question =====
# 題目會給一個數字 n 代表數字上限還有一個數字 s 代表總和目標值
# 然後要從 <= n 的所有質數(每個質數只能選一次)組一個 list 出來然後總和要 <= 目標
# 這邊答案可以有很多個回傳任一個就可以了
# 像是 7 的狀況可以回傳 2+5或2+3都可以

# ===== Thoughts =====
# 這題的限制非常的寬鬆所以可以先用埃拉托斯特尼篩法找出所有 ≤ n 的質數
# 然後再從小的質數開始累積並儲存遇到的質數，超過目標或是 n 的時候再回傳值就好了

# Method 1 - Directly Check
primes = list()
seen = set()
for val in range(2, 10 ** 6):
    if val in seen:
        continue
    primes.append(val)
    seen.add(val)
    for multi_val in range(val, 10 ** 6, val):
        seen.add(multi_val)

class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        curr = []
        curr_sum = 0
        for val in primes:
            curr_sum += val
            if val > n or curr_sum > s:
                break
            curr.append(val)

        return curr
