# ===== Question =====
# 題目給一個圓形的中心點跟半徑以及一個方形的左下跟右上兩個點的點座標
# 問說兩個圖形有沒有 overlap，這邊是嚴格的overlap，只要有一個點重疊就算

# ===== Thoughts =====
# 透過幾何的思考來想這問題，把圓貼在方形的邊上面轉一圈，圓心的軌跡可以形成一個圓角方形
# 只要圓心落在這個圓角方形裡面的話就代表一定是overlap
# 所以把這個圓角方形拆成幾部分：原始方形做(左右/上下)擴張半徑長度，以及四個點的四分之一圓
# 逐個去做條件判斷就可以了

# 還有另一種做法就是把圓心要比較的點先定位出來
# 分別對x, y 軸兩個面向去做同樣的區分，看看要定位的 x 跟 y 是在哪個區間
# 以 x 軸來說，兩個參考點 x1, x2，x1 左邊就取 x1，x2 右邊就取 x2，中間就取 xCenter  
# 接下來就去算這定位點跟圓心距離就可以了

# Method 1 - Rounded Corner Rectangle
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # left_buttom, right_top = (x1, y1), (x2, y2)
        # left_top, right_buttom = (x1, y2), (x2, y1)
        
        if (
            (x1 <= xCenter <= x2) and
            (y1 - radius <= yCenter <= y2 + radius)
        ) or (
            (x1 - radius <= xCenter <= x2 + radius) and
            (y1 <= yCenter <= y2)
        ):
            return True
        
        for x, y in itertools.product((x1, x2), (y1, y2)):
            if sqrt((x - xCenter) ** 2 + (y - yCenter) ** 2) <= radius:
                return True
        
        return False

# Method 2 - Set Point
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2))
        return (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2
