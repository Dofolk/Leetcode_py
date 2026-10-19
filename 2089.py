# ===== Question =====
# 題目會給一個常數 list 跟一個數字 target，然後對於 nums 做排序之後
# 把所有 target 數字的 index 都找出來，沒有 target 存在就回傳空集合

# ===== Thoughts =====
# 這一其實就是 quick sort 的一小步，去找比 target 小的就放在左邊
# 同時計算有多少 target，這樣就可以知道說 target 第一個出現的 index 在哪
# 以及說後續還要補多少的 index 也可以透過 count target 數量來獲得

# Method - Quick sort smaller part process
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count = 0
        smaller = 0
        
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                count += 1
        
        if count == 0:
            return []
        return list(range(smaller, smaller + count))
