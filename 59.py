# 這題是要做矩陣的螺旋擺放，按照數字順序羅選放到方陣裡面
# 做法就是直接做，做四個變數出來做位置的定位，然後調整位置逐個擺放就可以了
# 要注意的是一開始宣告出矩陣的時候要用 for 來做出二維的，不然如果是 [[]]*n 的話還是一維度的

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        up = left = value = 0
        right = down = n - 1
        
        while value != n**2:
            for col in range(left, right + 1):
                value += 1
                ans[up][col] = value
            for row in range(up + 1, down + 1):
                value += 1
                ans[row][right] = value
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    value += 1
                    ans[down][col] = value
            if left != right:
                for row in range(down - 1, up, -1):
                    value += 1
                    ans[row][left] = value
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return ans
