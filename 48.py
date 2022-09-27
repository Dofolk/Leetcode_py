# 這題是要做 rotation，把矩陣順時針轉90度
# 作法一就是四個四個做，先把角的部分作交替，然後就開始對下一個做變換
# 作法二就是先做轉置，然後把轉置後的每個 row 做反轉就可以了，因為轉置是轉180度，逐獵反轉就是迴轉90度

class Solution:
  
# 1
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for j in range(n//2+n%2):
            for i in range(n//2):
                tmp = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][n-1-j]
                matrix[i][n-1-j] = matrix[j][i]
                matrix[j][i] = tmp
                
# 2
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for l in matrix:
            l.reverse()
