# ===== Question =====
# 給定整數陣列 nums 和整數 x、k，每次操作可以將任一元素加 1 或減 1。
# 求最少操作次數，使陣列中至少有 k 個互不重疊、長度恰好為 x 的連續子陣列，且每個子陣列內的元素都相等（不同子陣列可以是不同數值）。

# ===== Thoughts =====
# 這題是就是先想一下每個 window 的 cost 是多少，然後有 cost 之後就可以用 dp 的方式來算
# dp 設計的方式就是當下位置的剛好放入 j 個區間所能得到的最低總成本
# 考慮前 i 個元素的最後一個位置，也就是 i - 1，有兩種選擇：
# - 不選這個位置：答案就是 best_j[i - 1]。
# - 讓一個區間在這裡結束：這個區間是 nums[i-x:i]，成本是 cost[i-x]；其餘 j-1 個區間必須放在它前面，成本是 best_{j-1}[i-x]。
# 實際的操作方式就是每次都比上一輪多選一個區間出來

'''
一開始，best 全部設為 0，表示還沒選任何區間時，成本都是 0。best[i] 代表在前 i 個元素中，放入目前數量的區間所需的最低成本。

接著更新 k 輪，每輪新增一個長度為 x 的區間。對每個起點 i，best[i] + cost[i] 表示先在前 i 個元素放好上一輪的區間，再接上從 i 開始、長度為 x 的新區間，兩者不會重疊。

這個結果使用到前 i+x 個元素，因此必須放在新陣列的索引 i+x。做法是在候選結果前面補上 x 個 inf，將索引向後移 x 格，也表示元素不足 x 個時無法放入新區間。上一輪的不可能狀態也會保留下來，所以第 j 輪自然會有前 j*x 個位置為 inf。

最後，使用 accumulate 搭配 min 計算累積最小值，讓每個位置保留截至該位置的最低成本，等同於允許最後幾個元素不被選入區間。

完成 k 輪後，best[-1] 就是在整個陣列中選出 k 個互不重疊區間的最低總成本。
'''

# Method - Sliding Window + DP
class Window:
    # Sliding window，用 sortedlist 來做到快速的數值更新
    def __init__(self, nums):
        self.mid, self.odd = len(nums) // 2, len(nums) & 1
        self.sort_list = SortedList(nums)
        self.low, self.total = sum(self.sort_list[:self.mid]), sum(nums)
    
    @property
    def cost(self):
        # 成本 = (高半總和 - 中位數 * 一半window的長度) + (中位數 * 一半window的長度 - 低半總和)
        # = 高半總和 - 低半總和 = high_half_sum - low_half_sum = (total_sum - low_half_sum) - low_half_sum
        # 中位數則是根據長度機偶再多補的
        return self.total - 2 * self.low - self.odd * self.sort_list[self.mid]
    
    def slide(self, remove, add):
        ls, mid = self.sort_list, self.mid
        # 新增的數比中位數小
        if add < ls[mid - 1]:
            self.low += add - ls[mid - 1]
        ls.add(add)
        # 移除的數比中位數小
        if remove <= ls[mid - 1]:
            self.low += ls[mid] - remove
        ls.remove(remove)
        self.total += add - remove
        return self.cost

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        win = Window(nums[:x])
        cost = [win.cost] + [win.slide(old, new) for old, new in zip(nums, nums[x:])]

        best = [0] * (len(nums) + 1)
        for _ in range(k):
            # 新的最佳解就是建立在上次的最佳解上多選一個 window 起來，所以用 inf * n 代表這個多選的 window
            new_best = [inf] * x + [b + c for b, c in zip(best, cost)]
            best = list(accumulate(new_best, min))
        return best[-1]
