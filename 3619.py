# ===== Question =====
# 題目會給一個 m x n 的二維陣列，當元素數值為 0 時代表是牆，以及一個數值 k
# 問說由牆壁隔起來的這些區域裡，區域的數值總和可以被 k 整除的個數有幾個

# ===== Thoughts =====
# 這題就是經典的圖形題，這邊就使用 BFS DFS 來操作
# 當踩到一個點之後就開始往下搜尋(BFS DFS 都可以)，並把有相連的區域都全部計算過
# 這邊要注意的是當踩過一個點之後就可以把該點設置成 0 當成是不用計算的地方
# 最後跑遍整個陣列就可以了

# Method 1 - BFS
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        stack = []
        ans = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total_val = grid[r][c]
                grid[r][c] = 0
                stack.append((r, c))

                while stack:
                    row, col = stack.pop()

                    new_row = row + 1
                    if new_row != m and grid[new_row][col] != 0:
                        stack.append((new_row, col))
                        total_val += grid[new_row][col]
                        grid[new_row][col] = 0

                    new_row = row - 1
                    if new_row != -1 and grid[new_row][col] != 0:
                        stack.append((new_row, col))
                        total_val += grid[new_row][col]
                        grid[new_row][col] = 0

                    new_col = col + 1
                    if new_col != n and grid[row][new_col] != 0:
                        stack.append((row, new_col))
                        total_val += grid[row][new_col]
                        grid[row][new_col] = 0

                    new_col = col - 1
                    if new_col != -1 and grid[row][new_col] != 0:
                        stack.append((row, new_col))
                        total_val += grid[row][new_col]
                        grid[row][new_col] = 0

                if total_val % k == 0:
                    ans += 1

        return ans


# Method 2 - DFS
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] == 0:
                return 0
            res, grid[row][col] = grid[row][col], 0
            res += dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)
            return res
        
        ans = 0
        for idx in range(m):
            for jdx in range(n):
                if grid[idx][jdx] != 0:
                    res = dfs(idx, jdx)
                    if res % k == 0:
                        ans += 1
        
        return ans
