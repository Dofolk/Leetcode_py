# 這題是給一堆數字，找出裡面只出現過一次的數字有哪些
# 做法就是直接 call counter，然後找一遍回傳就可以了

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        C = collections.Counter(nums)
        ls = list()
        for i in C:
            if C[i] == 1: ls.append(i)
        return ls
