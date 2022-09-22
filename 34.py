# 這題是要在 logn 的時間下從數列裡面找 target 出現的範圍，有就回傳範圍，沒有就回傳[-1,-1]
# 做法就是用 binary search，要找兩遍，一遍找出現的最小index，一遍找最大的

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        m = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if mid-1>=0 and nums[mid-1]==target:
                    r = mid - 1
                    continue
                m = mid
                break
        
        l, r = 0, len(nums) - 1
        M = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if mid+1<len(nums) and nums[mid+1]==target:
                    l = mid + 1
                    continue
                M = mid
                break
        
        return [m,M]
