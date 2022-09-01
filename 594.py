# 這題是要找最長的子序列，序列中只有包含兩個或以下的數字並且數字差不超過1
# 所以就是找數字差最近的兩個數字，那些可以湊到最長就對了

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        D = dict()
        M = 0
        for i in nums:
            if i in D: D[i] +=1
            elif i not in D: D[i] = 1
        for i in D.keys():
            if i+1 in D:
                M = max(M, D[i+1]+D[i])
            if i-1 in D:
                M = max(M, D[i-1]+D[i])
        return M
