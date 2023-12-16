# 這題是給一堆矩形的右上左下兩點的座標，然後從這些選定的區域裡面"均勻"隨機挑選一個點出來
# 作法有很多，但就是要確保每個點都是平等的被選取機率
# 所以這邊先做一個 sm 來記錄總共有多少點可以選
# 然後透過自由的選擇 sm 以內的數字來確保每個點選到的機會一樣
# 依照上面選到的數字去應對矩形，並從中選取點回船就可以了
# 順便講一下一個比較簡單的選法有問題的地方，不能先隨機選矩形再去抽點，因為每個矩形大小不一樣，會導致內部的點有不一樣的機率
# 舉例來說有兩個矩形，分別有4跟9個點，如果先選取矩形的話代表各有50%的機率選到一個矩形
# 這樣細分下去的話在4點矩形中的單點選取機率為0.5/4，但是在9點矩形則是0.5/9，會有明顯的差距出現

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects, self.ranges, sm = rects, list(), 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1,y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
