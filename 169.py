class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
      
# 找nums裡面最多的那個元素是哪個數字
# 有前提：最多的那個數字數量會超過整串的一半
# 所以這邊就是先sort之後取中姬那個出來就可以了，因為會超過一半所以取中間那個一定沒有問題
