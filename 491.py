# 這題是給一個 list 然後找出裡面所有的非遞減子序列
# 做法就是用 backtracking，用一個 set 來存結果，一個 ls 來記錄目前手上的非遞減子序列
# 透過 backtracking 來找看看下一個數字用錢一的最大值還是當下的值來做下一次的操作
# 每當跑到最後一個的時候就可以把結果存起來了


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        ls = []

        def backtrack(i, prev):
            if i == len(nums): 
                if len(ls) >= 2:
                    res.add(tuple(ls))
                return
            
            backtrack(i + 1, prev)
            
            if nums[i] >= prev:
                ls.append(nums[i])
                backtrack(i + 1, nums[i])
                ls.pop()

        backtrack(0, -inf)
        return list(res)
