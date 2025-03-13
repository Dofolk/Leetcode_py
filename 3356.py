# 這題是給一個數字 list nums 跟 queries，queries 的元素一定是 [left, right, value] 的形式，代表 nums[left~right(含)] 的每個位置都可以減 value
# 問最少在 queries 裡面照順序做幾個區間減法可以把 nums 變成全部都是 0(題目是給減法，這邊可以反向思考，從全 0 的 list 去累積 queries 的數值看有沒有每個都超過 nums)
# 
# === Thinking and Method ===
# 想法就是這題是要 nums 每個位置都要變成 0，這樣就可以從 nums 按照順序去找，對於 nums 每個位置找看看說當下位置的數值要跑多少 queries 才可以達到
# 要怎麼找當下位置可以有多少累積量？用 difference array 去紀錄 queries 每次做的範圍在哪以及數字是多少，用一個 arr 去紀錄
# 然後透過 prefix 的累積方式來記錄在每個位置可以達到的數值是多少
# 
# === Code Short Explanation ===
# 所以先給一個 for 來跑 nums 的位置，然後再用一個 while 來記錄 difference array 以及目前累積到 queries 第 k 個區間
# while 之後就更新他 prefix 的累積量，代表當下位置(idx)可以透過前 k 個 queries 累積達成
# 在 while 內一邊確認 prefix 的累積量有沒有達到 nums 當下位置的數值之外，也要確認 k 有沒有超過
# 要注意的是在 difference array 的紀錄中，要找 idx 跟 queries left 中最大的一個
# 這邊是要注意區間如果比當下位置(idx)還要前面的話，直接加在前面位置的話會累積不到，所以這邊就要選比較大的那個位置在記錄，這樣才可以累積到

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        L = len(nums)
        diff_arr = [0] * (L + 1)
        total_sum = 0
        k = 0

        for idx in range(L):
            while total_sum + diff_arr[idx] < nums[idx]:
                k += 1
                if k > len(queries):
                    return -1
                left, right, value = queries[k - 1]
                if right >= idx:
                    diff_arr[max(left, idx)] += value
                    diff_arr[right + 1] -= value
            total_sum += diff_arr[idx]
        return k
