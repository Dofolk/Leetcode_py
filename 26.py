class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
      
# 這題要把nums給整理掉，把重複的element移除
# nums後面的[:]會讓nums指定成global的那個
# 最後直接調整一下就好了
