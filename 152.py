# 這題是給一個陣列，然後找相乘之後會最大的子陣列(連續的子序列陣列)
# 做法就是用 M, m 來表示最大跟最小值，然後跑一遍陣列
# 最小值是用來記錄負數的，等負負得正翻身，最大值就是照著算
# 然後再比較的時候還要算上原本的值一起比，避免有最大最小都是0然後遇到數字卻沒辦法算出正確的值

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M = m = res = nums[0]
        for i in range(1,len(nums)):
            M, m = max(M*nums[i], m*nums[i], nums[i]), min(M*nums[i], m*nums[i], nums[i])
            res = max(M, res)
        return res
