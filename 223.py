# 這題是給 4 個座標點，找看看所覆蓋的面積是多少
# 做法就是兩個相加扣掉重疊的，所以就是直接先做相加，然後用 min 找出重疊的上界，用 max 找出重疊的下界
# 如果上下界剛好都可以是有長度的，那就扣掉重疊面積後回傳

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        S = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        x = min(ax2, bx2) - max(ax1, bx1)
        y = min(ay2, by2) - max(ay1, by1)
        if x > 0 and y > 0:
            S -= x*y
        return S
    
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - len(set(range(ax1,ax2)).intersection(range(bx1,bx2)))*len(set(range(ay1,ay2)).intersection(range(by1,by2)))
    
    
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        S = 0
        S += (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        over_x = self.check(ax1, ax2, bx1, bx2)
        over_y = self.check(ay1, ay2, by1, by2)
        return S-over_x*over_y
    
    def check(self, v1, v2, u1, u2):
        if v2 < u1 or u2 < v1: return 0
        if v1 >= u1 and v2 <= u2: return v2 - v1
        if u2 <= v2 and u1 >= v1: return u2 - u1
        if v2 <= u2 and v2 >= u1: return v2 - u1
        if u2 <= v2 and u2 >= v1: return u2 - v1
