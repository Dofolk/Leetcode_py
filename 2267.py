# ===== Question =====
# 題目給一個只有左右括號 () 的字元 2d array，然後要從左上的 (0, 0) 走到右下的 (m - 1, n - 1)
# 每次只能往左或往右走一格，目的是找到一條路徑讓走過的字元能組成合法的括號組
# 如果可以就回傳 True，找不到任何一條路的話就回傳False

# ===== Thoughts =====
# BFS/DFS 的題目 + 括號組的規則理解題，因為要找路徑所以 BFS 或 DFS 都可以做
# 但 python 這邊用 DFS 比較好，因為可以用 functools.cache()，因為有機會走到重複且同狀態的點
# 首先先排除絕對不可能的狀況: 1. 開頭是 ) ; 2. 結尾是 ( ; 3. 走路路徑是奇數步
# 一個 if 排除絕不可能的 case 之後，就是直接套上 BFS 或 DFS 的格式就可以了
# 在 BFS 或 DFS 裡面就是先做邊界檢查，然後再來看看左右括號的數量
# 在每一步左括號只能 >= 右括號，這樣才能確保可以做出合法的組合，可以分別記錄也可以紀錄總量差值
# 最後回傳結果就好

# Method1 - BFS
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False

        # bfs
        q = deque([(0, 0, 1, 0)]) # (row, col, count '(', count ')' )
        seen = set() # 存有看過的組合，減少重覆計算

        while q:
            comb = q.popleft()
            if comb in seen:
                continue
            seen.add(comb)
            row, col, left, right = comb
            if row == m - 1 and col == n - 1:
                if left == right:
                    return True
            for dx, dy in [(1, 0), (0, 1)]:
                next_row = row + dy
                next_col = col + dx
                if next_row >= m or next_col >= n:
                    continue
                next_left, next_right = left, right
                if grid[next_row][next_col] == '(':
                    next_left += 1
                else:
                    next_right += 1
                next_comb = (next_row, next_col, next_left, next_right)
                if next_comb not in seen and next_left >= next_right:
                    q.append(next_comb)
        
        return False


# Method 2 - DFS
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 == 1 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        
        @cache
        def dfs(row, col, count):
            count += 1 if grid[row][col] == '(' else -1
            
            if count < 0 or count > m - row + n - col - 1:
                return False
            
            if row == m - 1 and col == n - 1:
                return count == 0
            
            next_res = False
            if row < m - 1:
                next_res = next_res or dfs(row + 1, col, count)
            if not next_res and col < n - 1:
                next_res = next_res or dfs(row, col + 1, count)
            
            return next_res
            
        return dfs(0, 0, 0)
