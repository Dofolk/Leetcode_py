# 這題是要做矩陣的螺旋表示法
# 做法就是按照順序一個一個來做，用 while 來看看矩陣還有沒有存在，有就開始做
# 先把第一行 pop 出來存好，然後就繼續判斷矩陣存在與否，然後再把每個 row 的最後拿出來存......

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = list()
        
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        return ans
