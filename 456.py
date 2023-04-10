# 這題是給一個數字列表，然後找看看有沒有組合是 132 形式的，位置序號為 i < j < k，其對應位置的值比為: val(i) < val(k) < val(j) (就是一個山形的感覺)
# 做法就是用一個 min 列表來存開位置以前最小的值，然後用 stack 依序來存整個列表從面往前遇到的數字
# 當遇到列表的值比 min 的同位置的值大時就可以來檢查有沒有目標形式出現，檢查方法就是做 stack 操作，當 stack 有東西以及 stack[-1] 比最小值還小的時候就把值給 pop 掉
# 等都檢查完丟完之後就可以看看 stack 還有沒有東西，還有能不能符合目標形式(也就是說目前位置(index j)的值要比 stack 尾端(index k)的要大)，符合就可以做回傳了
# 如果一直到最後都沒有達成條件就回傳 false 結束整個執行

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        L = len(nums)
        if L < 3:
            return False
        
        stack = []
        min_array = [-1] * L
        min_array[0] = nums[0]
        
        for i in range(1, L):
            min_array[i] = min(min_array[i - 1], nums[i])
        
        for j in range(L - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        
        return False
