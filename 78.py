# 這題是要找所有子集合
# 作法幾種
# 用 backtrack 來操作，序號從0開始，每次做的東西有輛個，一個是要把數字加進來算，另一個就是我不要了
  # 透過要跟不要的兩種選擇就可以跑遍所有的可能性
# 另一種做法就是直接算，因為空集合是所有集合的子集合，所以一開始就先宣告一個空集合出來
  # 然後開始跑所有的數字，把每個數字及目前的 ans 都做一遍合併後存起來，就這是由小慢慢堆成大的子集合
  
# 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(combo, idx):
            if len(nums) == idx:
                ans.append(list(combo))
                return
            
            combo.append(nums[idx])
            backtrack(combo, idx + 1)

            combo.pop()
            backtrack(combo, idx + 1)
        
        backtrack([],0)
        return ans
      
# 2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            for i in range(len(ans)):
                ans.append( ans[i] + [n] )
        return ans
