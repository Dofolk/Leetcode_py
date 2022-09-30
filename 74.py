# 這題是要從二維矩陣內找目標值，而二維矩陣的每一個 row 都有做遞增排，且次一 row 的第一個值一定會比前一個 row的都要大
# 所以這題就是先找一下目標值會被放在哪一個 row，然後再看看有沒有在在 row 裡面找到目標值回傳就可以了

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] < target: continue
            else:
                if target in i: return True
                else: return False
        return False
