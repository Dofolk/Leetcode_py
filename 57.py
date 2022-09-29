# 這題是要把目標區間插入到區間序列裡，如果涵蓋到多個區間的話就做合併
# 做法就是看看區間在哪裡，分成三部分：左中右，還沒遇到比目標大的時候先放左邊，遇到都大的話就放右邊，然後中間就更新一下區間的邊界就可以了

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        s, e = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1]<s:
                left.append(i)
            elif i[0]>e:
                right.append(i)
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left+[[s,e]]+right
