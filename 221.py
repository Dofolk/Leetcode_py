# 這題是要在給定的陣列中找最大的方形是多大
# 做法就是事先對每個 column 做 row 向加總，看看每個row目前有多長的邊長
# 然後跳到下一個 column 之後就開始看前一個 col 對應位置有沒有東西，有的話就看一下累積寬度(width)有沒有比目前最大的邊長還要長(k)
# 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        n, m = len(matrix), len(matrix[0])
        width = [0] * n
        k = 0

        for j in range(m):
            max_conti_k = 0
            conti_k = 0
            for i in range(n):
                if matrix[i][j] == '1': width[i] += 1 #累積長度用
                else: width[i] = 0
                if width[i] > k: #確認說累積長度有沒有達標
                    conti_k += 1
                    max_conti_k = max(max_conti_k, conti_k)
                else: conti_k = 0
            if max_conti_k > k: k += 1 #以前面的當基礎看看目前的 col 可以產生多大的正方形，如果比之前產生更大的那就把邊長加一下
        
        return k*k
