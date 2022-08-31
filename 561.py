# 這題是給一個 list，然後每兩個數字做配對成 pair，選取 pair 中比較小的數字做相加，最後盡可能最大化這個總和
# 做法就是先做排序，然後依照順序兩個兩個一對就可以達到最大了

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        v = 0
        for i in range(0,len(nums),2):
            v += nums[i]
        return v
