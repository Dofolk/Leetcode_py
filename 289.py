# 這題就是做康威生命遊戲的模擬
# 做法就是複製一個陣列，然後依據複製陣列的每個格子周圍一圈的生命數來改變原本陣列的值就可以了
# 康威生命遊戲的維G: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        direction = {(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)}
        m, n = len(board), len(board[0])

        copy = [ [ board[row][col] for col in range(n) ] for row in range(m) ]

        for i in range(m):
            for j in range(n):
                
                life = 0
                for D in direction:
                    r, c = i+D[0], j+D[1]
                    if (r < m and r >=0 ) and (c < n and c >=0 ) and copy[r][c]==1:
                        life += 1
                if copy[i][j] == 1 and (life < 2 or life > 3):
                    board[i][j] = 0
                if copy[i][j] == 0 and life == 3:
                    board[i][j] = 1
        
