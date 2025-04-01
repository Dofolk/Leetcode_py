class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        max_reward, min_reward = max(nums), 1
        houses = len(nums)
        
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            stolen = 0

            idx = 0
            while idx < houses:
                if nums[idx] <= mid_reward:
                    stolen += 1
                    idx += 2
                else:
                    idx += 1
            
            if stolen >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1
        
        return min_reward
