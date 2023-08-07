# 這題是給圓心跟半徑，然後隨機給圓內一點
# 做法就是隨機取半徑長跟角度，然後用三角函數做就可以了
# 但是不知道為啥第二個解會報錯

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        R = math.sqrt(random.uniform(0, self.r ** 2))
        degree = random.uniform(0,1) * 2 * math.pi
        x = self.x + R * math.cos(degree)
        y = self.y + R * math.sin(degree)
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

# solution 2
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        R = random.uniform(-self.r, self.r)
        degree = random.uniform(0,1) * 2 * math.pi
        x = self.x + R * math.cos(degree)
        y = self.y + R * math.sin(degree)
        return [x,y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
