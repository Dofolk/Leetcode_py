# 這題是要做 list 的 wiggle sort，也就是要 1<2>3<4>5....(這邊的數字指的是位置index，代表該index的數值大小)
# 做法就是先 sort，然後依需插進去就好

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])-1
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]
