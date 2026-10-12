# ===== Question =====
# 題目會給一個數字 list nums 還有一個數字 k，問經過以下操作任意次數之後取 k 個數字做平方和最大是多少
# 操作就是任意選不同位置 i 跟 j，然後 nums[i] = nums[i] AND nums[j] 以及 nums[j] = nums[i] OR nums[j]
# AND 跟 OR 是 bit 操作

# ===== Thoughts =====
# 這題就是先想一下 AND 跟 OR 的操作特性，AND 會把 1 給刪掉， OR 會保留 1
# 然後因為 AND OR 可以操作任意次，所以其實可以再經過多次操作後把數字做成 2 ^ n - 1
# 這樣操作一定可以達到的，nums[j] 缺漏的 bit 就找找其他有該 bit 的 nums[i] 來補就可以了
# nums[i] 就會把該 bit 挪出去並保留剩下的 bits
# 所以這邊可以考慮在固定長度的 bit length 下做出盡可能大的數字們
# 選用的數字也是越大越好，因為 (a + b)^2 >= a^2 + b^2
# 最後就是去算每個 bit 位置有出現幾次 1，然後開始去組數字出來就可以了

# Method - Directly Check
MOD = 10 ** 9 + 7

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        M = max(nums)
        b = 1
        basic = []
        
        while b <= M:
            basic.append(b)
            b <<= 1
        
        bit_len = len(basic)
        bit_count = [0] * bit_len

        for num in nums:
            for idx, b in enumerate(basic):
                if num & b:
                    bit_count[idx] += 1
        
        vals = [0] * k
        for idx in range(bit_len):
            for jdx in range(min(k, bit_count[idx])):
                vals[jdx] += basic[idx]
        
        ans = 0
        for val in vals:
            ans = (ans + val * val) % MOD
        
        return ans
