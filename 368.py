# 這題是給一個 list，然後找一下最長的因數組合
# 做法就是用字典，然後先做排序，讓數字由小到大慢慢地堆積上去
# 先找數字小的最長可以做多，然後存起來讓後面去用

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1: set()}
        nums.sort()
        for x in nums:
            S[x] = max((S[d] for d in S if x % d == 0), key = len) | {x}
        return list(max(S.values(), key = len))
