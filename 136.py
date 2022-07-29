class Solution:
  
# Solution 1
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            value = nums[i]
            nums[i] = float('inf')
            if value not in nums:
                return value
            nums[i] = value
         
# Solution 2
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        if i == 0:
            return nums[0]
        while i >= 0:
            if nums[i] == nums[i-1]:
                i -= 2
            if nums[i] != nums[i-1]:
                return nums[i]
              
# 找出list中只有出現過一次的那個值
# 第一個方法就是每個值都走過一遍，先把走到的值存起來、變成inf，然後再看看值有沒有重複，有重複就把inf還回去原始值，在找下一個
# 第二個方法就是先對list做排序，然後從後面開始往前兩個兩個找(一定成雙成對)
