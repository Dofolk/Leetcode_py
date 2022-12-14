# 這題是給一個陣列，然後要間隔找相加最大為多少，間隔至少一格(不相鄰)
# 做法就是先架好基本的前 3 個，然後開始往前 1 個或 2 個相加(如果往前3個的話就可以直接做往前單一間隔的跳點相加了)
# 最後就是看倒數兩個哪個比較大就可以了

class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0: return 0
        if L <= 2: return max(nums)
        
        m = [0]*L
        m[0] = nums[0]
        m[1] = nums[1]
        m[2] = nums[0] + nums[2]

        for i in range(3,L,1):
            m[i] = max(nums[i] + m[i - 2], nums[i] + m[i - 3])
        
        return max(m[-1],m[-2])
