# 題目是，給一個 m x n 的陣列，然後先往右上走，走到牆邊後就往右或往下折反，接下來往左下走，走到牆邊就改成往下或往右折返
# 最後按照走的順序將數字輸出成列表回傳
# 做法就是照著玩，用一個參數 direction來記錄自己要往哪個方向跑(這邊1是右上)，這邊也把矩陣的column當成x軸，row當成y軸
# 然後先把自己當下位置的數值存好，然後去確認有沒有在牆邊需要換方向的(17.25行)，處理好方向之後就往該方向前進直到結束

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ls = list()
        m, n = len(mat), len(mat[0])
        direction = 1
        pos_x, pos_y = 0, 0

        for i in range(m*n):
            ls.append(mat[pos_y][pos_x])

            if direction == 1:
                if pos_x >= n-1 or pos_y <= 0:
                    direction = -1
                    if pos_x == n-1: pos_y += 1
                    else: pos_x += 1 
                else:
                    pos_x += 1
                    pos_y -= 1
            else:
                if pos_x <= 0 or pos_y >= m-1:
                    direction = 1
                    if pos_y +1 < m: pos_y += 1
                    else : pos_x += 1
                else:
                    pos_x -= 1
                    pos_y += 1
        
        return ls
