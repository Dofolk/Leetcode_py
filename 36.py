# 這題是檢查數獨的盤面有沒有符合規則，每一列每一行都不會重複的數字出現，每個3*3的方塊也沒有重複地出現
# 作法很簡單，直接雙重 for 把要確認的都確認一遍就可以了 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count3 = [ [ [],[],[] ] , [ [],[],[] ] , [ [],[],[] ] ]
        
        for i in range(9):
            count1 = set()
            count2 = set()
            for j in range(9):
                if board[i][j] in count1:
                    return False
                elif board[i][j] != ".":
                    count1.add(board[i][j])
                if board[j][i] in count2:
                    return False
                elif board[j][i] != ".":
                    count2.add(board[j][i])
                if board[i][j] in count3[i//3][j//3]:
                    return False
                elif board[i][j] != ".":
                    count3[i//3][j//3].append(board[i][j])
        
        return True
