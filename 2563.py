# === Description ===
# 題目給一個數列 nums 及 最大值 upper, 最小值 lower，問有幾個組合可以 nums[i] + nums[j] 介於 upper 跟 lower，並且 i < j
#
# === Thought ===
# 題目的要求 i < j 其實可以忽略掉，重點在於相加要在範圍內，所以可以去找相加在範圍內的組合就可以了
# 當找到這些組合時就自然符合 i < j，因為組合抽出來一定一個是 index 大的，一個是小的，大的當 j 就好
# 所以這邊就可以先用 sort 直接按數字大小來排序，然後從左右兩邊開始往內尋找
# 左右兩邊相加的數字超過範圍就縮小右邊界，以左邊界當基準來看
# 當相加之後落在範圍內就代表說以左邊界數字來說，這個左右邊界內的數字都可以選擇，所以可以計算這麼多個組合
# 然後就依照左邊界往右移動找下一個範圍
# === Code ===

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.count(nums, upper) - self.count(nums, lower - 1)

    def count(self, nums, target):
        count = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1
        return count
