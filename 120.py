# 這題是給一個三角形的陣列，然後要找總和最少的路徑
# 想法就是抄底，最底層 兩兩相比，小的往上一層加上去，一直加到最頂點就是最小的路徑和了
# 寫法就是直接做，雙重 for loop 直接弄下去就可以收工了

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:        
        H = len(triangle)
        for i in range(1,H):
            for j in range(H-i):
                triangle[H-i-1][j] += min(triangle[H-i][j],triangle[H-i][j+1])
        return triangle[0][0]
