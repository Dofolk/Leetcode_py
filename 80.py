# 這題不用回傳東西，只要把給的 list 重複出現3次以上的東西給移除就好，然後只能在常數的額外空間做操作
# 做法就是從 list 尾端往前計數看有沒有超過，有的話就 remove，沒有就不理他

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count, p1 = 1, len(nums)-1
        
        while p1>0:
            if nums[p1]==nums[p1-1]:
                count += 1
                if count >=3:
                    nums.remove(nums[p1])
                    count -= 1
                    p1 -= 1
                    continue
            if p1>0 and nums[p1]!=nums[p1-1]:
                count = 1
            p1 -= 1
