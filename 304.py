# 這題是給一個 2D 陣列，然後找出特定範圍的值總和是多少 (要在 O(1) 裡做完)
# 這邊就是先做加總，把所有值都給他往右下加下去，讓每個點都是自己所有左上的總和
# 這樣給範圍之後就是用 A-B-C+BnC 來算值出來就可以了
# 參考https://leetcode.com/problems/range-sum-query-2d-immutable/solutions/2104244/python-easy-with-explanation/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix : return
        n, m = len(matrix), len(matrix[0])
        self.s = [ [ 0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.s[i][j] = matrix[i-1][j-1] + self.s[i][j-1] + self.s[i-1][j] - self.s[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row2, col2 = row2 + 1, col2 + 1
        return self.s[row2][col2] - self.s[row2][col1] - self.s[row1][col2] + self.s[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
