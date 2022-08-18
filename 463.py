# 這題就是給2D地圖，1代表小島，0代表水域，然後來算一下地圖裡面小島部分編長是多少(以正方形來看)
# 做法就是雨到小島就先+4，然後判斷一下左邊跟上面有沒有相連，有就一個地方各扣2，這樣就可以為出整個大島嶼了

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        v = 0
        col = len(grid)
        row = len(grid[0])
        for i in range(col):
            for j in range(row):
                if grid[i][j] == 1:
                    v += 4
                    if i > 0 and grid[i-1][j] == 1:
                        v -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        v -= 2
        return v
