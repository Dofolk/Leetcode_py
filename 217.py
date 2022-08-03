# 這題要找 list 裡面有沒有重複的值
# 第一個方法就是先 sort，然後再逐個往前比對有沒有一樣的
# 第二個方法就是用 python 的 in 來找

class Solution:

# Solution 1
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = len(nums)-1
        
        while i > 0:
            if nums[i]==nums[i-1]:
                return True
            else:
                i -= 1
        
        return False
      
# Solution 2
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        while nums:
            tmp = nums.pop()
            if tmp in s:
                return True
            else:
                s.add(tmp)
        return False
