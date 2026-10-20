# ===== Question =====
# 題目會給一個常數 list nums，其長度為 n，然後對於 n 的所有因數 k 來說
# 把 nums 切割成小區間段，且每個區間段長度為 k，並且對於每個小區間段做循環的 rotation 之後
# 能讓整個 nums 呈現遞增(>=)的話，就稱 k 為 sortable
# 問給定的 nums 所有 sortable 的因數總和加起來是多少

# ===== Thoughts =====
# 這一題直接窮舉，可以先建立每個長度的因數表 factors
# 然後要讓整個 nums 都是遞增的，所以每個區間段最大限度符合以下的條件
# 出現一個 peak + peak 後的數值不能比前一個區間段小 + peak 後到區間結束這段期間的值要比區間左端點小
# 所以這邊就可以先去找原本 nums 裡面哪裡會發生 peak (right)
# 接下來再針對每個 peak 跟區間段作條件檢查就好

# Method - Enumeration
M = 100001
factors = [[] for _ in range(M)]
for val in range(2, M):
    for multi in range(val, M, val):
        factors[multi].append(val)

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        right = [n] * n # 紀錄每個 idx 右邊變成遞減後產生 peak 的位置在哪裡
        for idx in range(n - 2, -1, -1):
            if nums[idx] > nums[idx + 1]:
                right[idx] = idx
            else:
                right[idx] = right[idx + 1]
        
        ans = 0
        # 確認原數列是不是本來就遞增了，+1是1為因數的狀況
        if right[0] == n:
            return sum(factors[n]) + 1
        
        def fn(k):
            # prev_max 紀錄前一個小區間段的最大值，用來檢查全域遞增的條件
            prev_max = 0
            # 對於每個長度為 k 的區間段，看看區間段左端點的下一個 peak 在哪裡 
            for r in range(k - 1, n, k):
                left = r - k + 1
                peak = right[left]
                # 下一個 peak 超過右邊界時代表這個區間是遞增的
                # 這邊就會要去檢查左端點有沒有大於前一段的 max
                if peak > r:
                    if nums[left] < prev_max:
                        return 0
                    prev_max = nums[r] # 更新區間最大值
                
                # 區間段內有 peak 發生時
                else:
                    if (
                        right[peak + 1] < r or 
                        # 下一個 peak 還在區間內，兩個 peak 沒辦法循環
                        nums[peak + 1] < prev_max or 
                        # 在遞減之後的質比前一個區間段還要小，這樣沒辦法做到全域遞增
                        nums[r] > nums[left]
                        # peak 發生後優邊比左邊還大，右邊循環到左邊去時沒辦法做到區間遞增
                    ):
                        return 0
                    prev_max = nums[peak] # 更新區間最大值
            
            return k
        
        for f in factors[n]:
            ans += fn(f)
        
        return ans
        
