# 這題是跟198一樣的題目，都是要間隔間搶錢，看怎樣搶比較多，但是這題的頭尾是相鄰的
# 所以這題的做法就是變成兩個去做，頭不搶跟尾不搶的兩個 list 分別去找看看怎樣會比較多錢

class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0: return 0
        if L <= 3: return max(nums)
        
        def sol(nums: List[int]) -> int:
            rob, not_ = 0, 0
            for num in nums:
                rob, not_ = not_ + num, max(rob, not_)
            return max(rob, not_)
        
        return max(sol(nums[1:]),sol(nums[:-1]))
