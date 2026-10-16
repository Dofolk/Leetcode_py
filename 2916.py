# ===== Question =====
# 題目會給一個常數 list，然後找出所有子序列並計算每個子序列有多少不同的元素
# 接著把每個子序列不同元素的數量做平方後相加並回傳

# ===== Thoughts =====
# 這題要直接轉去找靈神(https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/solutions/2502897/yi-bu-bu-ti-shi-ni-si-kao-ben-ti-pythonj-zhhs/)
# 這邊是透過一步一步來確認每多一個元素之後數值怎麼變化
# 平方合的差距會是 (c+1)^2 - c^2 = 2c + 1
# 然後透過線段樹來動態紀錄及 query 每個區間的數值

# Method for 2916 - Segment Tree
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sum = [0] * (n * 4) # sum[o] 增加 add × 區間長度。
        todo = [0] * (n * 4) # todo[o] 記錄尚未傳給子節點的增加量，等需要往下查詢時再處理。
        

        def do(o: int, l: int, r: int, add: int) -> None:
            sum[o] += add * (r - l + 1)
            todo[o] += add

        # o=1  [l,r] 1<=l<=r<=n
        # 把 [L,R] 加一，同时返回加一之前的区间和
        def query_and_add1(o: int, l: int, r: int, L: int, R: int) -> int:
            if L <= l and r <= R:
                res = sum[o]
                do(o, l, r, 1)
                return res

            m = (l + r) // 2
            add = todo[o]
            if add:
                do(o * 2, l, m, add)
                do(o * 2 + 1, m + 1, r, add)
                todo[o] = 0

            res = 0
            if L <= m: res += query_and_add1(o * 2, l, m, L, R)
            if m < R:  res += query_and_add1(o * 2 + 1, m + 1, r, L, R)
            sum[o] = sum[o * 2] + sum[o * 2 + 1]
            return res

        ans = s = 0
        last = {}
        for i, x in enumerate(nums, 1):
            j = last.get(x, 0)
            s += query_and_add1(1, 1, n, j + 1, i) * 2 + i - j # 2c + 1，同時也會把 1 都塞給前面的區間內
            ans += s
            last[x] = i
        return ans % 1_000_000_007

# Method for 2913 - 簡化版 segment tree or 暴力 for loop 硬解(因為限制數字 <= 100)
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 1
        prev = 1
        dp = [1]
        last = {}
        last[nums[0]] = 0

        for idx in range(1, len(nums)):
            new_dp = [0] * (idx + 1)
            ls = last.get(nums[idx], -1)
            curr = prev + 2 * (sum(dp[ls + 1:])) + idx - ls
            ans += curr
            for jdx in range(ls + 1):
                new_dp[jdx] = dp[jdx]
            for jdx in range(ls + 1, idx):
                new_dp[jdx] = dp[jdx] + 1
            new_dp[-1] = 1

            prev = curr
            dp = new_dp
            last[nums[idx]] = idx
        
        return ans
