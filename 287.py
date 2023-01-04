# 這題是給一個數字列表，找看看哪個數字重複出現了
# 做法就是用 set 來記錄拿到的數字，然後整個走過一遍就可以了
# 或是用 counter 也可以

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        C = collections.Counter(nums)
        for v in C:
            if C[v] >= 2:
                return v
     
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for v in nums:
            if v in s: return v
            else: s.add(v)
