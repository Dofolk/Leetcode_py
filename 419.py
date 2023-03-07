# 這題是給一個二維陣列，去算裡面的戰艦有幾艘，每艘戰艦只會直或橫放，不會重疊
# 想法就是只要往上或往左有東西就不計算，因為不會重疊到，所以可以用這方法來計算數量

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    var = 1
                    if (r > 0 and board[r-1][c] == 'X') or (c > 0 and board[r][c-1] == 'X'):
                        var = 0
                    count += var
        return count
