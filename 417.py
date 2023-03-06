# 這題是會給一個二維的陣列(島嶼)，左+上兩邊面臨太平洋，另外兩邊是大西洋，每個格子表示地形高度，現在假設下雨了，那些格子的水可以同時流進兩個海洋
# 想法就是做路徑搜尋(DFS)，從最邊邊的幾個往內去找，用 1 跟 2 來代表不同的海域，如果可以讓某個點同時被 1 2 經過的話就代表說這個格子的水可以留到兩個海裡去，就可以存起來了
# 但是遇到同樣地方來的或是高度變低的時候，就直接跳過，因為我們是要去找水流所以不能低流向高以及不能同個海域洄流
# 所以用一個一維的打平的陣列來存目前每個位置可以留到哪個海域
# 最後在每個邊點跑一次 DFS 就可以了

class Solution:
    def pacificAtlantic(self, M: List[List[int]]) -> List[List[int]]:
        if not M:
            return M
        
        x, y = len(M[0]), len(M)
        ans, dp = [], [0] * (x * y)
        
        def dfs(i: int, j: int, w: int, h: int):
            idx = i * x + j
            if dp[idx] & w or M[i][j] < h:
                return
            dp[idx] += w
            h = M[i][j]
            if dp[idx] == 3:
                ans.append([i, j])
            if i + 1 < y:
                dfs(i + 1, j, w, h)
            if i > 0:
                dfs(i - 1, j, w, h)
            if j + 1 < x:
                dfs(i, j + 1, w, h)
            if j > 0:
                dfs(i, j - 1, w, h)
        
        for i in range(y):
            dfs(i, 0, 1, M[i][0])
            dfs(i, x - 1, 2, M[i][x - 1])
        for j in range(x):
            dfs(0, j, 1, M[0][j])
            dfs(y - 1, j, 2, M[y - 1][j])

        return ans
