# 這題是要找出重複的值，並找出缺少的值
# 做法就是先排序，找出重複的值，最後再判斷缺少的值是不是頭跟尾

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        miss = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                dup = nums[i]
            elif nums[i]>nums[i-1] + 1:
                miss = nums[i-1] + 1
        if nums[len(nums)-1]!=len(nums):
            miss = len(nums)
        return [dup,miss]
