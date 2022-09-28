# 這題是要把給定的區間做合併，能合併的就合併，不能合併的就分開來
# 做法也算簡單，照著做就可以了，判斷一下最後面的值有沒有比較小，有的話就可以做merge，沒有的話就可以新增新的一個區間了

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = list()
        for i in intervals:
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
        
        return ans
