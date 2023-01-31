# 這題是要找看有沒有遞增的三個數字，而且 index 也是要遞增的
# 做法就是用兩個變數存目前遇到的前兩個小的數字，有遇到小的就依照大小更新
# 如果遇到比這兩個都大的話就可以通過 if 判斷，直接回傳 True，否則一直做到最後都沒用到就離開 for 回傳 False

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
