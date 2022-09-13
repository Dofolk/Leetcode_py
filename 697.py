# 這題是要找子序列，要找援序列出現最多次的數字所構成的最短子序列
# 做法就是左又逼近，紀錄每個走過的值的次數，一直更新每個數字走到最遠的index
# 最後就可以相減找最小

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i,v in enumerate(nums):
            if v not in left: left[v] = i
            right[v] = i
            count[v] = count.get(v,0) + 1
        degree = max(count.values())
        ans = len(nums)
        for i in count:
            if count[i]==degree:
                ans = min(ans, right[i]-left[i]+1)
        return ans
