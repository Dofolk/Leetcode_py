# 這題是給一個 2D array 的地圖，說哪裡有水(1)跟土地(0)，然後回傳另一張地圖，說每個土地最近的水源在幾格之外
# 這邊算幾格的方式就是每次走路只有上下左右 4 個方向去做計算
# 所以先做一個地圖出來看看那些格子是 水(0) 跟沒有走過的 土地(-1)
# 接著 BFS 從每個水源出發，看看走到那些土地要幾步路

class Solution:
    def highestPeak(self, water: List[List[int]]) -> List[List[int]]:
        m, n = len(water), len(water[0])
        stack = deque()
        for i in range(m):
            for j in range(n):
                water[i][j] -= 1
                if water[i][j] == 0:
                    stack.append((i,j))
        while stack:
            x, y = stack.popleft()
            if  x > 0 and water[x - 1][y] == -1:
                water[x - 1][y] = water[x][y] + 1
                stack.append((x - 1, y))
            if  y > 0 and water[x][y - 1] == -1:
                water[x][y - 1] = water[x][y] + 1
                stack.append((x, y - 1))
            if x < m - 1 and water[x + 1][y] == -1:
                water[x + 1][y] = water[x][y] + 1
                stack.append((x + 1, y))
            if y < n - 1 and water[x][y + 1] == -1:
                water[x][y + 1] = water[x][y] + 1
                stack.append((x, y + 1))
        return water
