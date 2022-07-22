class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)-1
        while a<=b:
            i = (a+b)//2
            if nums[i]==target:
                return i
            if nums[i]<target:
                a = i + 1
            else:
                b = i - 1
        return a
                
# 找到對的位置塞target進去，回傳index
# targe跟list值一樣的話就回傳最小的那個index
# 所以這邊考慮大小作夾擠，讓a,b +-1去做縮小，然後讓a先動，這樣確保說a的位置是好的
# 縮到a>b的時候就是找到的時候(因為理當來說a不能比b大)
