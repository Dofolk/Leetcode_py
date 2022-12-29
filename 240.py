# 這題是給一個二微陣列，然後找看看給定值有沒有在裡面
# 做法就是直接每個 row 跑一遍做 in 的確認就可以了
# 或是每個 row 做 binary search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i: return True
        return False
