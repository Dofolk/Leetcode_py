# 這題是找三個數字加總離目標最近的總和是多少
# 做法跟數字加總差不多，一樣用 two pointer來操作，只是變成要多更新一個數字記錄目前離最近的是多少

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = float('inf')
        val = float('inf')
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
                if abs(target - s) < m:
                    val = s
                    m = abs(target - s)
                    
        return val
