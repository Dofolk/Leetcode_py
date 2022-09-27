# 這題是要找 permutation 的所有可能性，然後有可能出現重複的
# 做法就是用 backtrack去操作，不過操作的對象是數字的 count
# 把數字都拿完配上 backtrack 的算法就可以達到組合的需求

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        def backtrack(combo):
            if len(combo) == len(nums):
                ans.append(list(combo))
                return
            for n in count:
                if count[n] > 0:
                    combo.append(n)
                    count[n] -= 1
                    backtrack(combo)
                    combo.pop()
                    count[n] += 1
        
        backtrack([])
        return ans
    
