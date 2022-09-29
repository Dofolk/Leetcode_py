# 這題是要找從左上走到右下的路徑有幾種，但是中間會有障礙物
# 做法就是把高中的時候學到的方法寫出來，底部沒障礙的話就寫 1，然後逐漸往上堆疊，看左邊數字有多少就加起來，遇到障礙物就給他掛上 0

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[m-1][n-1]
