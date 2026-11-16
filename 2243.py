# ===== Question =====
# 給定數字字串 s 和整數 k，當字串長度大於 k 時，從左到右每 k 個字元分成一組，最後一組可以不足 k 個。
# 將每組的各位數字相加，再把各組的總和轉成字串，依序串接成新的 s。
# 重複操作直到長度不超過 k，回傳最後的字串。

# ===== Thoughts =====
# 這題就是重複同樣的操作做到達成目標就好
# 選擇可以使用的方法有兩個，一個是 recursion，另一個是 while
# 但基本上都是在操作題目給定的流程而已

# Method 1 - Recursion
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s
        
        ans = ""

        for idx in range(0, n, k):
            curr = 0
            for count in range(k):
                pos = count + idx
                if pos < n:
                    curr += int(s[pos])
            ans += str(curr)
        
        return self.digitSum(ans, k)

# Method 2 - Single while
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            k_count = 1
            curr = 0
            next_s = ""
            for ch in s:
                if k_count > k:
                    next_s += str(curr)
                    k_count = 1
                    curr = 0
                curr += int(ch)
                k_count += 1
            next_s += str(curr)
            s = next_s
        
        return s
