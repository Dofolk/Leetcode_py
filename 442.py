# 這題是給一個數字列表，每個數字可能會出現 1 次或 2 次，然後把所有出現 2 次的數字全部回傳
# 做法就是用 counter 做計數後再去逐個檢查

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return res
        
        c = collections.Counter(nums)

        for i in c:
            if c[i] > 1:
                res.append(i)
        
        return res
