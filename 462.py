# 這題是給一個數字列表，然後每次只能對一個數字加減1，看看要最少幾次可以讓所有數字相同
# 做法就是先找出中位數之後再去做差距的相加
# 20261102 Note: 找中位數的原因是因為這樣就可以在更進一步降低計算的數量，因為中位數那個數字不用做任何加減

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = nums[len(nums)//2]
        count = 0
        for num in nums:
            count += abs(num - med)
        
        return count
