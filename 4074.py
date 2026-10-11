# ===== Question =====
# 題目會給一個目標數字，問說能不能透過連續三個費波那契序列的元素總和得到目標值

# ===== Thoughts =====
# 這題就是直接去操作費波那契就可以了
# 使用三個數值分別代表費波那契需要用到的三個數值
# 再去檢查總和有沒有符合就好了

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
