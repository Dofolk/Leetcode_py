# ===== Question =====
# 題目給一個數字列表 arr 跟一個目標數字 target
# 求兩個總合為target的 不相交 subarray 長度總和最小是多少
# 舉例來說 [2,3,4,5], target = 5，答案就是3 [2,3]跟[5]長度和是3

# ===== Thoughts =====
# 想法有二，一個是prefix + dp，一個是sliding window + dp
# 主要就是用 dp[jdx] 來記錄 jdx 以前最短的一個 subarray 多短
# 然後透過當下計算加總前面的紀錄就可以求得答案
# (因為要找兩個 subarray，所以就是遍歷之後把前面的一段記錄起來，另一段則是邊走邊計算)

# prefix 的想法是因為要找subarray，所以可以透過prefix 來快速找到subarray 的總和
# 所以這邊就要找一個 jdx 使得與現在位置 idx 的關係變成 prefix[idx] - target = prefix[jdx]
# 這樣就是 jdx + 1 ~ idx 這區間段總和就是target
# 接著是想如何找到這一個 jdx ，在從頭開始往後遍歷的同時可以透過hash table 來記錄遇到過的prefix
# 這樣就可以根據 idx 快速找到對應的 jdx
# 最後就是 dp 的環節，dp[jdx] 意思是儲存 jdx 之前遇到最短的sub array是多短
# 這樣在遍歷的時候計算 dp[jdx] + (idx - jdx) 就可以得到最小的長度和了

# 另一個想法就是sliding window + dp，是另一種計算 subarray 的方式
# 這時候我們就是從頭遍歷一次，然後透過 sliding window 來確認總合為 target 的長度是多少
# 就是用 sliding window 的 left 當成是 prefix 的 jdx
# 也就是我往前找的話要在哪裡找第一段的最短長度

# Method 1 - prefix + dp
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pos = {0: -1}
        n = len(arr)
        s = 0
        ans = n + 1
        min_l = n
        for i, x in enumerate(arr):
            s += x
            if s - target in pos:
                j = pos[s - target]
                length = i - j
                ans = min(ans, length + (n if j == -1 else arr[j]))
                min_l = min(min_l, length)
            arr[i] = min_l
            pos[s] = i
        return -1 if ans == n + 1 else ans


# Method2 - sliding window + dp
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        left = 0
        total = 0
        n = len(arr)
        ans = n + 1
        
        dp = [n] * (n + 1)
        
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            dp[right + 1] = dp[right]
            if total == target:
                ans = min(ans, right - left + 1 + dp[left])
                dp[right + 1] = min(dp[right], right - left + 1)
        
        return -1 if ans == n + 1 else ans
