# 這題是要找 peak，也就是要找比左右兩邊數字都大的位置，回傳其中一個就好
# 做法就是二分法，去看看有沒有比左右大，有就回傳，沒有的話就按照目前位置與前一個位置比較來決定往左往右

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        L, R = 0, N-1
        while L <= R:
            mid = (L+R)//2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == N-1 or nums[mid] > nums[mid + 1]):
                return mid
            if mid == 0 or nums[mid] > nums[mid - 1]:
                L = mid + 1
            else:
                R = mid - 1
        return -1
