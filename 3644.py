# ===== Question =====
# 題目會給一個整數 list nums，所有數字是 0 ~ n - 1 的 permutation
# 然後要在特定的限制下做 swap，最終把 list 排序呈遞增序列
# 條件是選擇不同位置 idx jdx，找一個 k 讓 nums[idx] & nums[jdx] == k，兩個位置就能互換
# 問說這個 k 最大是多少

# ===== Thoughts =====
# 原本題目寫的不是很好，但就是要找一個 k 通用在所有的 swap 操作上面
# 首先要做 swap 讓 list 遞增，這樣的話就要先知道哪些數值沒有在遞增序列的正確位置上
# 要把這些數值做交換 + AND 操作 + 共用一個 k => 直接把所有數值做 AND 運算找到 k
# 這樣我就可以知道說所有數值共通的 AND 結果是哪個，然後就可以用這個 k 做互換達成目標
# 就算這邊到最後求得的 k 是一個已經排序好的數值也沒關係
# 有需要時他可以當中繼站，中繼 idx jdx 之間的 swap

# Method - Check Relationship of max/min with left/right end node
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        base = None

        for idx, num in enumerate(nums):
            if idx != num:
                if base is None:
                    base = num
                else:
                    base &= num
        
        return 0 if base is None else base
