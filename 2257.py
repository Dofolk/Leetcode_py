# 這題是給牆(W, walls)及看守者(G, guards)的位置，每個看守者可以顧上下左右4個方位看過去的所有格子，但是遇到牆就看不到
# 請問：給定 m x n 的這個範圍內搭配上給定的看守者及牆的位置後，有多少地方是沒有人看守的
# 做法就是做一個空的 2d list，來記錄現在每個位置是甚麼，然後把看守者(2)及牆(2)的位置標上去
# 接著就把 4 個方向都訂出來，以看守者的角度出發，對 4 個方向做 while 來更新格子的數字
# 遇到牆或是超過範圍的就 break
# 最後在計算 0 的數量有多少就好，這邊在計算的時候用sum for就好了，counter不會比較快(Time out)

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # make an empty array to store each position's status(0 for no guard, 1 for guard, 2 for guardians and walls)
        block = [[0] * n for _ in range(m)] # 不能用 [[0]*n]*m，因為會pass by assignment，list是mutable object，所以在裡面的list是全部都一樣的

        # update the guardians and walls position into the array
        for G in guards:
            block[G[0]][G[1]] = 2
        for W in walls:
            block[W[0]][W[1]] = 2
        # 4 directions and start from the sight of guardians
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for gx, gy in guards:
            for dx, dy in dir:
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    if  x < 0 or x > m - 1 or y < 0 or y > n - 1 or block[x][y] == 2 :
                        break
                    block[x][y] = 1
                    
        return sum(row.count(0) for row in block)
