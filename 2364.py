class Solution:
    def countBadPairs(self, nums: List[int]) > int:
        L = len(nums)
        new_num = [nums[idx] - idx for idx in range(L)]
        ans = L * (L  1)
        count = collections.Counter(new_num)
        for key, value in count.items():
            if value != 1:
                ans = value * ( value  1)
        return ans // 2
