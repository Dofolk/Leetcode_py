# 這題是給一個上到下左到右都是遞增的陣列，然後找出第K大的數字值是多少
# 做法是使用到 bisect 的函數以及用 binary searc
# 因為給的陣列是遞增的，所以可以把(0,0)跟(-1,-1)當成是最大跟最小，用 mid 配合 bisect_right 來逐行找出每列要把mid放在第幾個位置給總起來就知道mid在陣列裡面多大了
# 然後再去更新最左右邊的數字就可以逐步逼近最後的答案了

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        L, R, m = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(v):
            count = 0
            for i in range(m):
                x = bisect_right(matrix[i], v)
                count += x
            return count
        
        while L < R:
            mid = (L + R) // 2
            if less_k(mid) < k:
                L = mid + 1
            else:
                R = mid
        
        return L
