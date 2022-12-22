# 這題會給目標值以及數字數量，看看在規定的數量及 1-9 只能個使用一次的狀況下，組成目標值的組合有哪些(同數字組合順序不同的，算同個組合不能重複出現)
# 做法就是用 backtrack (類似39.40題)，首先先判斷遺下目標值有沒有大於數量(因為不能重複用)以及45(1+...+9=45)
# 然後就開始做 backtrack，如果剩餘=0及長度剛好就把組合存起來，如果剩餘<0或長度太長就 return 不再往下做
# 這邊在 recursive 的時候用 i + 1 以避免重複使用值

class Solution:
    def combinationSum3(self, length: int, target: int) -> List[List[int]]:
        if length >= target or target > 45: return []

        res = []
        ls = [i for i in range(1,10,1)]

        def backtrack(remain: int, idx: int, combo: List[int]) -> None:
            if remain == 0 and len(combo) == length:
                res.append(list(combo))
                return
            elif remain < 0 or len(combo) > length: return
            for i in range(idx, 9, 1):
                if ls[i] in combo: continue
                combo.append(ls[i])
                backtrack(remain-ls[i], i + 1, combo)
                combo.pop()
        
        backtrack(target, 0, [])
        return res
