# ===== Question =====
# 題目會給一個常數 list nums，其長度為 n，整個數列是 0 ~ n - 1 的 permutation
# 問說透過幾次 (向左 rotate 一格 or 數列反轉) 可以讓整個 list 遞增
# 如果無法做到就回傳 -1

# ===== Thoughts =====
# 這一題要做 sort，在 0 ~ n - 1 的 permutation 可以把題目分成兩種狀況
# 一種是本來就遞增遞減的序列然後按順序 rotate，另一種則是怎樣都無法做到遞增遞減
# 這樣的話就先確認是不是第一種，確認方式也很簡單，就是找 0 或是 n - 1 當起始點
# 然後去檢查選用的點去拚出遞增或遞減的樣子，然後再去比對有沒有跟遞增數列一樣就可以了
# 遞減的也同樣道理，就是要記得把整個數列反過來就是了
# 如果通過遞增或遞減的檢查時，就去更新操作的次數
# 遞增最小操作次數就是 直接左 rotate到底 or 反轉->左rotate->反轉(用在要左 rotate的位置很右邊的時候)
# 遞減最小操作次數就是 直接左 rotate到底 -> 反轉 or 先反轉->左 rotate到底
# 如果前面兩項都沒辦法符合代表本身就不是遞增或遞減的數列，只能透過 swap 做到，所以直接回傳 -1

# Method - Sorting Check
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = float('inf')
        target = list(range(n))

        idx = nums.index(0)

        if nums[idx:] + nums[:idx] == target:
            res = min(res, idx, n - idx + 2)
        
        reverse_nums = nums[::-1]
        reverse_idx = reverse_nums.index(0)
        if reverse_nums[reverse_idx:] + reverse_nums[:reverse_idx] == target:
            res = min(res, reverse_idx + 1, n - reverse_idx + 1)
        
        if res == float('inf'):
            return -1
        return res
