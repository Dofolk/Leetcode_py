class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i;
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hash and hash[c]!=i:
                return[i,hash[c]]
