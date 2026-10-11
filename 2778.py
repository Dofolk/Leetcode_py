# ===== Question =====
# 題目一個序號從 1 開始且長度為 n 的常數 list
# 序號位置(idx) 如果能整除長度 n (ie: n % idx == 0)就叫他特別數字(special)
# 問所有特別數字的平方合是多少

# ===== Thoughts =====
# 這題就是直接計算就可以了，直接檢查每個位置是不是 special，是就算總和不是就下一位

# Method 1 - Directly Check
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for idx in range(1, n + 1):
            if n % idx == 0:
                ans += nums[idx - 1] ** 2
        
        return ans
