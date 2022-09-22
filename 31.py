# 這題是要做一個東西叫 next permutation
  # 意思是說，如果數列是遞減的那就直接reverse，沒有的話看一下哪邊(問題點)是開始沒有遞減的(也就是從尾巴往前找看看哪裡沒有遞增)
  # 然後把問題點往後找相近的值做交換，交換之後就把後面的數列做成遞增的(反向遞減)
  # 147531->157431->151347
# 做法就是尾巴往前找，確定好哪邊有問題之後就操作交換跟reverse()

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = len(nums) - 1
        while p1 > 0 and nums[p1] <= nums[p1 - 1]:
            p1 -= 1
        if p1 == 0:
            nums.reverse()
            return
        
        while nums[p2] <= nums[p1-1]:
            p2 -= 1
        
        nums[p1-1], nums[p2] = nums[p2], nums[p1-1]
        
        nums[p1:] = nums[len(nums) - 1 : p1-1 : -1]
