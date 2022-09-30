# 這題是要找左上到右下的最小路徑
# 做法跟有障礙物的一樣，做累加就可以了
# 累加的方式是看看左邊跟上面哪個數字小就加哪個，一路加到底就可以得到最小的了

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
