# 這題是給 4 個長度為 n 的整數字串，然後從中挑選各一個數字相加起來看有沒有等於 0 ，目標是計算總共有多少組這樣的組合
# 做法是直接做，用 counter 來計算前兩個字串總和跟出現次數，然後再用後兩個相加後去找看看有沒有遇到相同的數字，最後再加總就可以了

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums = collections.Counter(c+d for c in nums3 for d in nums4)
        return sum(sums.get(-(a+b), 0) for a in nums1 for b in nums2)
