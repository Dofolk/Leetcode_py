class Solution:
  
# Solution 1
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

# Solution 2
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        target = n*(n+1)//2
        return target-sum(nums)
      
# 這題是要找出 List 裡面所缺少的數字是哪個
# 第一種作法就是先排序之後再一個一個找
# 第二種做法就是全部加起來之後相減找出差值
