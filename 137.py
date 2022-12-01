# 這題是給一個陣列，找出只出現一次的數字是多少
# 做法就是直接算數量，用counter做計算就可以收工了

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        D = Counter(nums)
        for i in D:
            if D[i] == 1:
                return i
