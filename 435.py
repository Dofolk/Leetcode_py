# 這題是給一個區間的列表，然後算移除幾個可以讓整個列表是 non overlapping
# 做法先做排序，然後看每個區間的左端點如果比前一個還大就可以更新前一個的數字並且留下，不然就計算要移除的數量+1

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev, count = float('-inf'), 0
        for i in intervals:
            if i[0] >= prev:
                prev = i[1]
            else:
                count += 1
        return count
