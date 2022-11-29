# 這題是給一個陣列，有 O 跟 X，然後看看哪些 O 被包圍起來，被包圍起來要改成 X (就是一個圍棋的概念)
# 想法就是，為一活路的方法就是找到一條路跑到邊界去，所以先從邊界把 O 改成 S(solve)
# 然後用 dfs 的方式從邊界往內去找到所有有相鄰的 O 並通通改成 S
# 最後再把 S 改成 O，其他都改成 X

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        
        row, col = len(board), len(board[0])

        def dfs(i,j):
            if i > 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'S'
                dfs(i-1, j)
            
            if j > 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'S'
                dfs(i, j-1)
            
            if i < row-1 and board[i+1][j] == 'O':
                board[i+1][j] = 'S'
                dfs(i+1, j)
            
            if j < col-1 and board[i][j+1] == 'O':
                board[i][j+1] = 'S'
                dfs(i, j+1)
            
            return
        
        for i in range(row):
            if board[i][0] == 'O':
                board[i][0] = 'S'
            if board[i][col-1] == 'O':
                board[i][col-1] = 'S'
        
        for j in range(col):
            if board[0][j] == 'O':
                board[0][j] = 'S'
            if board[row-1][j] == 'O':
                board[row-1][j] = 'S'
        
        for i in range(row):
            if board[i][0] == 'S':
                dfs(i, 0)
            if board[i][col-1] == 'S':
                dfs(i, col-1)
        
        for j in range(col):
            if board[0][j] == 'S':
                dfs(0, j)
            if board[row-1][j] == 'S':
                dfs(row-1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                
