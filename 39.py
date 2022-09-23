# 這題給定一串數字序列及一個目標，看目標能不能用序列的數字相加組合出來
# 做法是用 backtrack，從頭一個一個做，這邊設計的概念是在剩餘，看看剩餘多少，往下找能不能找到剩餘的數或是組合出來
# 所以在往下找的時候就用 for 迴圈來做，逐漸移動 index 來看看能不能滿足剩餘數
# 總結來說，backtrack的函數就會需要幾個輸入，一個是剩餘多少要給，一個是目前所擁有的數字組合，還有一個index來看看說我這一輪要從哪邊開始找起跟計算

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates.sort()
        ans = []
        
        def backtrack(remain, idx, combo):
            if remain == 0:
                ans.append(list(combo))
                return
            elif remain <0:
                return
            for i in range(idx, len(candidates)):
                combo.append(candidates[i])
                backtrack(remain-candidates[i], i, combo)
                combo.pop()
            
        backtrack(target, 0, [])
        return ans
