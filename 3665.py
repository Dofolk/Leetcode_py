# ===== Question =====
# 題目給一個只有 0 跟 1 的二維陣列，從左上角出發，計算抵達右下角的不同路徑數量。
# 遇到 0 可以向右或向下移動；遇到 1(鏡子)則必須轉向，向右變向下、向下變向右。
# 回傳所有合法路徑的總數，答案對 10^9 + 7 取餘數。

# ===== Thoughts =====
# 這題算路徑是從基本款的左上走到右下的變形，每次在走的時候變成多去考慮它的來源跟會不會變向
# 但這個考慮變向的部分可以在每個格子去處理，所以整體的還是用 DP
# 這邊分別去記錄從上來的路徑數量跟從左邊來的路徑數量
# 遇到前一步(不管上面來的還是左邊來的)有 1 的時候就去抓相對應轉向的路徑數量，如果是 0 就直接合併計算(沒有轉向問題))
# 最後回傳右下角格子的上面來的跟左邊來的路徑兩個總和是多少就好
# 這還可以再調整一下寫法(ref. Mathod2)，不在 DP 紀錄左邊來的跟上面來的，直接在更新的時候另外拉出來處理就好
# method 1 更偏向 rolling dp 一點的作法，method 2 則是多一個 dp 來處理前一個 row 的結果(執行效率好一點)

# Method 1 - DP
MOD = 10 ** 9 + 7
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # (from left, from top)
        dp = [(0, 0) for _ in range(n)]
        dp[0] = (1, 0)

        for col in range(1, n):
            if grid[0][col - 1] == 1:
                break
            dp[col] = (1, 0)
        
        for row in range(1, m):
            if grid[row - 1][0] == 1:
                dp[0] = (0, 0)
            else:
                dp[0] = (0, sum(dp[0]))
            for col in range(1, n):
                curr_left = dp[col - 1][1] + (dp[col - 1][0] if grid[row][col - 1] == 0 else 0)
                curr_top = dp[col][0] + (dp[col][1] if grid[row - 1][col] == 0 else 0)
                dp[col] = (curr_left, curr_top)
        
        return sum(dp[-1]) % MOD

# Methos 2 - DP
MOD = 10 ** 9 + 7
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [0] * n
        dp[0] = 1

        for row in grid:
            prev_row, dp, left = dp, [0] * n, 0

            for idx, top in enumerate(prev_row):
                if row[idx] == 0:
                    dp[idx], left = top + left, left + top
                else:
                    dp[idx], left = left, top
            
        return dp[-1] % MOD
