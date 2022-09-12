# 這題是要對一個給定 m*n 的圖做 3*3 濾波，如果沒有 3*3 的話就依照能有多少就多少
# 做法就是暴力解，一個一個做，要記得判斷有沒有超出 index 範圍

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img),len(img[0])
        ans = [[0]*C for i in img]
        for i in range(R):
            for j in range(C):
                count = 0
                for nr in range(i-1,i+2):
                    for nc in range(j-1,j+2):
                        if 0<=nr<R and 0<=nc<C:
                            ans[i][j] += img[nr][nc]
                            count += 1
                ans[i][j] //= count
        return ans
