# 這題是把所有0都移動到最後面，然後非零的部分按照順序往前放就好了
# 方法就是用 two pointer 來做

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        
        
        while p1 < len(nums):
            if p2 > len(nums)-1:
                nums[p1] = 0
                p1 += 1
            elif nums[p2]!=0:
                nums[p1] = nums[p2]
                p1 += 1
                p2 += 1
            else:
                p2 += 1
