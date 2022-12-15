# 這題是給一個矩陣，有 1 的地方代表有陸地，然後算一下總共有幾個島
# 做法就是用 DFS 把矩陣有相連的地方都找出來變成 s
# 先確認一下是不是從 1 開始做出發，是的話就代表有個島，然後把所有島範圍都變成 s 做標記，所以下次遇到有s的地方就知道之前有算過數量了

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1': return
            grid[i][j] = 's'
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        
        return count
