# 這題是要做二分搜尋，給一個遞增的樹列，找看看需要的值有沒有在裡面
# 做法就是用 while 來做，對分看看有沒有遇到值，然後比大小來調整對分的區間

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i<j:
            p = (i+j)//2
            if nums[p] == target:
                return p
            if nums[p] < target:
                i = p + 1
            if nums[p] > target:
                j = p 
        
        return -1
