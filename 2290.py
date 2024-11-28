# 這題是給一個 2d array，裡面有些地方有石頭有些沒有，這些石頭可以被拿走，試問：從左上走到右下的路徑上須拿走最少幾顆石頭才能達到目的地
# 很典型的 BFS 題目，只是要轉換一下，把每個位置當成節點，其"四個方向"就是邊，然後透過一個 2d array 來記錄抵達該位置目前最少須拿走的石頭數量
# 這邊在 BFS 搜尋的時候可以透過判斷原始位置是不是 0 來決定下一個位置要從 queue 的最左邊放進去還是丟在後面，有點貪婪的想法在裡面，可以讓速度快一點

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dis = [[100000] * n for _ in range(m)]
        q = deque()
        dis[0][0] = 0
        q.append((0,0))
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n:
                    new_dis = dis[x][y] + grid[x][y]
                    if new_dis < dis[next_x][next_y]:
                        dis[next_x][next_y] = new_dis
                        # greedy thought, when meeting 0 it will be first deal with
                        if grid[next_x][next_y] == 0:
                            q.appendleft((next_x, next_y))
                        else:
                            q.append((next_x, next_y))
        return dis[m - 1][n - 1]
            
            
