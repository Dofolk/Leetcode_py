# 這題是給一個數字 list ，然後要找裡面兩個數字 XOR 的最大結果
# A xor B = target <=> A xor target = B，用這個規則來做，把 target 當成一個過濾的值，去逐個討論每個 bit 存在的可能
# 那判斷的條件就是 target 要在過濾後的集合裡面，這樣才算符合上面的敘述

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        M, mask = 0, 0

        for i in range(31, -1, -1):
            mask |= 1 << i
            fixed = {n & mask for n in nums}
            
            tmp = M | (1 << i)
            
            if any(fix ^ tmp in fixed for fix in fixed):
                M = tmp
        
        return M
