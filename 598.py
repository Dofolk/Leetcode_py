# 這題是給一個 m*n 的零矩陣，然後給一堆範圍 ops，每次在範圍內的元素數字+1，然後最後回傳數字最大的個數有幾個
# 作法就很簡單，找最小的範圍就可以了，因為範圍最小就一定都會被加到，然後當沒有給範圍的話每個值都是0，所以就回傳 m*n

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m*n
        m1, m2 = float('inf'), float('inf')
        for i in ops:
            m1 = min(i[0], m1)
            m2 = min(i[1], m2)
        return m1*m2
