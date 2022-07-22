class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[index] = nums[j]
                index += 1
        return index
            
# two pointer作法
# 設定index為最後紀錄到的長度，讓j跑遍所有數值
# 同val就跳過，不同的話就原地紀錄(index控制位置)
