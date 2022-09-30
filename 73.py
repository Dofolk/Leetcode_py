# 這題是要把矩陣內的 0 做十字轟炸
# 作法是先定位出0的位置，然後依據位置把行列的值全部變成0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            matrix[i] = [0]*n
        for j in col:
            for i in range(m):
                matrix[i][j] = 0
