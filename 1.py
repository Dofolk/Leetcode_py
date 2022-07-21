class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i;
        for i in range(len(nums)):
            c = target - nums[i]
            if c in hash and hash[c]!=i:
                return[i,hash[c]]
            
# 建立一個hash matrix來記錄有過那些值
# 然後在一個一個去比對有沒有存在差值，在python裡面可以用 'in' 來快速找到有沒有存在
