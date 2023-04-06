# 這題是給一堆長形的氣球，然後將他們橫擺在平面上並給上他們的起始結尾的x座標，然後從x軸向上垂直發射箭矢，最少幾根可以射爆全部的氣球
# 做法就是先用排序依照位置前後排好，然後看第一個氣球的尾端在哪裡，用前一顆氣球的尾端及其餘的氣球前端來判斷重疊的氣球有幾個，超過的話就代表需要多一隻箭矢來用


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count, tail = 1, points[0][1]
        
        for op, ed in points:
            if tail < op:
                tail = ed
                count += 1
        
        return count
