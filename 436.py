# 這題是給一個區間的列表，然後找每個區間的右邊總共有幾個區間(重疊的就不算是在右邊)
# 做法就是用區間帶頭的數字搭配位置來做排序，然後用 bisect 來計算數量，如果數量沒有超過總長度就記錄下來，不然就是已經是最右邊的了，那就直接紀錄 -1

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = list()
        ls = sorted((v[0], i) for i, v in enumerate(intervals))
        L = len(ls)
        for k in intervals:
            r = bisect.bisect_left(ls, (k[1], ))
            res.append(ls[r][1] if r < L else -1)
        return res
