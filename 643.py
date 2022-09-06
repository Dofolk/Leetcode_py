# 這題是找長度為k的連續元素子序列總和，找最大的那個
# 做法就是先找第一個子序列，然後開始往後做移動，一個一個慢慢走到最後

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        M = s
        for i in range(k,len(nums)):
            s += nums[i]-nums[i-k]
            if s>M: M=s
        return M/k
