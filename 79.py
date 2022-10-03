# 這題是要做 matrix 的字串搜尋，從給定的矩陣中找看看有沒有目標的單字，要相鄰且不可重複使用
# 做法就是用 backtrack，往四個方向去搜尋，然後走過的點就給他改變一下值就可以往下繼續找了，找完之後記得要把值放回來，避免直接死掉
# 然後做 backtrack之前可以先做確認，確認矩陣跟目標單字所需的字母跟數量是符合的

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        
        D = dict()
        for i in range(m):
            for j in range(n):
                if board[i][j] in D: D[board[i][j]]+=1
                else: D[board[i][j]] = 1
        D_word = dict()
        for i in word:
            if i in D_word: D_word[i] += 1
            else: D_word[i] = 1
        for c in D_word:
            if c not in D or D_word[c]>D[c]:
                return False
        def bt(i,j,idx=0):
            if len(word) == idx: return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or word[idx]!=board[i][j]: return False
            tmp = board[i][j]
            board[i][j] = '0'
            if bt(i+1,j,idx+1): return True 
            if bt(i,j+1,idx+1): return True
            if bt(i-1,j,idx+1): return True
            if bt(i,j-1,idx+1): return True
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bt(i,j):
                        return True
        return False

    
