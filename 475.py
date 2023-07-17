# 這題是給房子位置資訊以及暖爐的位置資訊，找出可以讓所以家庭都溫暖的暖爐最小作用範圍是多少
# 做法就是用家庭位置去做搜尋，用 two pointers 的概念去找看看每個家庭離他最近的暖爐位置是哪個
# 所以用一個 for 來跑遍所有家庭，在每個家庭位置時用 while 來檢查看看暖爐位置要不要往前更新去找最近的暖爐位置

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        
        mr, heat = 0, 0
        
        for i, house in enumerate(houses):
          # 如果下一個暖爐可以離比較近的話就用 while 來更新暖爐 heat 的位置數據
            while heat + 1 < len(heaters) and\
             abs(heaters[heat] - house) >= abs(heaters[heat + 1] - house):
                heat += 1
            mr = max(mr, abs(heaters[heat] - house))
        
        return mr
