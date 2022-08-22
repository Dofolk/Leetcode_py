# 這題是要找出最長有多長是連續出現 1
# 遇到 1 就加進 list 裡面，遇到0就開始算看看 ls 有多長然後重置

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ls = list()
        v = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ls.append(1)
            elif nums[i] == 0:
                v = max(v, len(ls))
                ls = list()
        return max(v, len(ls))
