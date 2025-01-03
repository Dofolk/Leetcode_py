# 這題是給一個常數 list，然後切成兩段(段落至少都要有個數字)，算看看左邊段落比右邊段落大的次數有幾次
# 作法一是用 prefix 把 nums 給整理好，接著就是計算段落總和、比較跟紀錄
# 在做法一的第二個 for 裡面可以發現用到最後面的 sum 數字，所以可以先計算總合
# 又可以知道說經過移項就是去找看看對半分得數字就是標準，如果能超過就過了
# 所以做出第二個做法，先加總對半分，在開始逐個加數字看看有沒有比較大

# ver1
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return len(nums) // 2 if nums[0] != 0 else len(nums) - 1
        L = len(nums)
        for idx in range(1, L):
            nums[idx] += nums[idx - 1]
        count = 0
        for idx in range(L - 1):
            if nums[idx] >= nums[L - 1] - nums[idx]:
                count += 1
        return count

# ver 2
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return len(nums) - 1 if nums[0] == 0 else len(nums)//2
        left = 0
        right = (sum(nums)+1)//2
        count = 0
        for idx in range(len(nums)-1):
            left += nums[idx]
            if left >= right:
                count += 1
        return count
