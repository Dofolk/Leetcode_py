# 這題是要找出一個數字的因數們最靠近的，因數a,b 使得 a*b = n & min(b-a)
# 第一個做法就是暴力解，找出所有因數再取中間值
# 第二個做法就是從 sqrt(n) 往下找，能整除就可以回傳了

class Solution:
  
# Solution 1
    def constructRectangle(self, area: int) -> List[int]:
        ls = [x for x in range(1,area+1) if not area%x]
        return [ls[len(ls)//2], area//ls[len(ls)//2]]
# Solution 2
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5), 0, -1):
            if not area%i:
                return [area//i,i]
