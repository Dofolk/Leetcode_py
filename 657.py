# 這題是要做機器人的移動，看經過一系列的移動之後機器人會不會回到原點
# 做法就是算上下左右各自的移動數量，算總量就可以確定說會不會回到原點了
# 這邊就直接用 count() 來計算總量

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        x += moves.count('U')
        x -= moves.count('D')
        y += moves.count('L')
        y -= moves.count('R')
        return x==y==0
