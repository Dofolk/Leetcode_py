# ===== Question =====
# 題目給一個正整數列表 nums 跟一個正整數 x，每次操作取 nums 的頭或尾去扣 x
# 如果可以讓 x 扣到 0 的話就紀錄操作次數，如果不管如何都沒辦法的話就回傳 -1
# 最後藥布馬回傳 -1，要不就是最小化操作操數並回傳

# ===== Thoughts =====
# 這題操作就是在處理 prefix suffix 的操作，所以第一個就是從 prefix suffix 出發
# 計算 prefix後逐漸增加 suffix 的長度，去找對應的prefix長度，一直更新結果就可以了
# 另一種想法就是我要找最短的 prefix suffix 和剛好等於 x
# ==反過來想==> 找prefix suffix 中間夾起來的那段，找最長的那段並且總和等於 sum(nums) - x
# 從頭遍歷一次，把 sliding window 掛在中間那段 sub array
# 逐漸累積 value 並且檢查有沒有超過 sum(nums) - x，超過舊更新 window 的左邊界

# Method1 - prefix suffix
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        prefix = list(itertools.accumulate(nums))
        n = len(nums)
        if prefix[-1] < x:
            return -1
        elif prefix[-1] == x:
            return n
        
        idx = bisect_left(prefix, x)
        if prefix[idx] == x:
            ans = idx + 1
        else:
            ans = n + 1
        suffix_sum, suffix_len = 0, 0
        
        while suffix_sum < x:
            suffix_len += 1
            suffix_sum += nums[n - suffix_len]
            diff = x - suffix_sum
            if diff < 0:
                break
            elif diff == 0:
                ans = min(ans, suffix_len)
                break
            
            while idx >= 0:
                if prefix[idx] == diff:
                    ans = min(ans, suffix_len + idx + 1)
                elif prefix[idx] < diff:
                    break
                idx -= 1
        
        if ans == n + 1:
            return -1
        return ans

# Method 2 - Sum - x
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        if target == 0:
            return n
        elif target < 0:
            return -1
        
        res = -1
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]
            while current_sum > target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum == target:
                res = max(res, right - left + 1)
        
        return n - res if res != -1 else -1
