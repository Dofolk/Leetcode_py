# 這題是要做數字的加總，然後同一組數字就只存一次
# 所以在操作的時候也適用 backtrack，只是在操作的時候要變成是再往下找一個數字，而不是自己那一個
# 在設計 backtrack 的時候就要多一些判斷式，判斷index有沒有比較大以及數字一樣，這種狀況我們就是留到比較後面處理


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def backtrack(remain, combo, idx):
            if remain == 0:
                ans.append(list(combo))
                return
            for next_idx in range(idx,len(candidates)):
                
                if next_idx > idx and candidates[next_idx] == candidates[next_idx - 1]:
                    continue
                
                p = candidates[next_idx]
                if remain - p < 0:
                    break
                
                combo.append(p)
                backtrack(remain - p, combo, next_idx + 1)
                combo.pop()
        
        backtrack(target, [], 0)
        
        return ans
