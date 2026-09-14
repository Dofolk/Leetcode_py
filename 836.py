# ===== Questions =====
# 題目的意思是會給兩個矩形，然後判斷舉行有沒有重疊(overlap)，點跟線的重疊不算重疊
# 題目會給兩個舉行的左下跟右上這兩個點的座標位置

# ===== Thoughts =====
# 這題用幾何的角度去想像，要重疊就是等於矩形A的右上點會在矩形B左下點的右上方
# 同時矩形A的左下點也要在矩形B右上點的左下方
# 或者是直接做反向思考，固定矩形B的位置，思考哪些地方不可能重疊並且排除掉他們也是一個可行方法
# 矩形B右上點的右上方以及左下點的左下方，這兩個地方如果出現完整的矩形A，那就不可能重疊了
# 判斷的方法就是A的右上點在B的左下方(B左下點的左下)，以及A的左下點在B右上點的右上方(B右上點的右上)

# Method 1 - 直接判斷重疊

class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    return (
        rec1[0] < rec2[2] and rec1[1] < rec2[3] and
        rec1[2] > rec2[0] and rec1[3] > rec2[1]
    )

# Method 2 - 反向排除

class Solution:
  def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    return not (
            rec1[2] <= rec2[0] or rec1[3] <= rec2[1] or
            rec1[0] >= rec2[2] or rec1[1] >= rec2[3]
        )
