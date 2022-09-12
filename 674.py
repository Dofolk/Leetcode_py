# 這題是要找最長的"連續"子序列
# 連續很重要，可以考慮用 two pointer 來做
# 做法就是用 two pointer 逐個找並紀錄最長的長度是多少
# 最後還要記得再多做一次確認長度，避免說剛好整個 seq 是嚴格遞增的

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        p1,p2 = 0,1
        M = 0
        for i in range(len(nums)):
            if p2>=len(nums):
                break
            if nums[p2]<=nums[p2-1]:
                M = max(M,p2-p1)
                p1 = p2
            p2 += 1
        M = max(M,p2-p1)
        return M
