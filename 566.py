# 這題要自己寫一個 reshape() 出來
# 給定的矩陣大小如果不等於預期的 row*column 的時候就回傳原本的矩陣(所以用 if 判斷一下就可以了)
# 接下來就是先把矩陣變成 1*(size) 的 list，然後再依據預期的行列數去分割就可以了

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M = len(mat)*len(mat[0])
        if M != r*c:
            return mat
        L = list()
        for i in mat:
            L += i
        ls = list()
        for i in range(r):
            ls.append(L[i*c:(i+1)*c])
        
        return ls
