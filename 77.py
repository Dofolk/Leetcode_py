# 這題是要做組合，從 1~n 的數字做出長度為 k 的組合出來
# 做法就是 backtrack，當長度為k時就存結果下來，然後就開始用 for 跑後面的 index

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        ls = list(range(1,n+1))

        def backtrack(combo,idx):
            if len(combo) == k:
                ans.append(list(combo))
                return
            for i in range(idx,n):
                combo.append(ls[i])
                backtrack(combo, i+1)
                combo.pop()
        
        backtrack([], 0)
        return ans
      
# 2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = list(range(1,n+1))
        return list(map(list,combinations(ls,k)))
