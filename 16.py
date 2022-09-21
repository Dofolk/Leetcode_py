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
# 2
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        m = float('inf')
        start = 0
        end = len(nums) - 1
        
        while start < end:
            l = start + 1
            r = end - 1
            m_tmp = float('inf')
            while l <= r:
                mid = (l+r)//2
                s = nums[start] + nums[mid] + nums[end]
                if abs(target - s) < abs(target - m_tmp):
                    m_tmp = s
                if s > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if abs(target - m_tmp) < abs(target - m):
                m = m_tmp
            if m_tmp > target:
                end -= 1
            else:
                start += 1
        
        return m
