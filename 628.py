# 這題是要找最大的3個數字相乘數字
# 做法就是先排序，然後找最後面三個(全正最大) 跟 前兩個及最後一個的乘積(雙最負及一正)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
