# ===== Question =====
# 題目給一個 m x n 二維陣列 grid，然後只能往右或往下走，要從左上走到右下
# 問說現在每一條路徑上所有數字做 XOR 得到的數字最小可以小到多少
# 限制條件: 單邊長最多1000， mxn 最多也 1000，數字最大 1023，皆正整數

# ===== Thoughts =====
# 這題就是首先考慮 XOR 的特性，他沒有遞增遞移性質，所以沒辦法直接套用累積和的 DFS
# 所以就會變成每走一格就要記錄所有可能的數字，並把這堆數字往下往後推移
# 所以這邊可以用 DP 來做，因為只能往右往下的方向移動，所以可以用滾動式的一維 DP 來做紀錄
# DP 的內容就是一個 set，紀錄目前位置從上過來的事多少，然後再考慮從左邊過來的所有可能
# 全部都計算一遍之後就去更新 DP，最後回傳最小就好
# 這邊也可以使用 DFS，但一樣就是要把當下的數字傳遞下去，遇到右下角的時候再更新 XOR 最小數字就好
# 另一中方式就是用 bit mask 來處理，簡單來說就是用一個很長的 bit (1024位的 bit) 來記錄遇到過哪些數字
# 然後跟 DP 一樣走過所有可能，但更新方式就是用比較快速的 bit mask 來操作
# 每個 bit 代表數字，最右邊的 bit 代表數字 0，往左一個就是數字 1，以此類推到1023
# 透過 bit mask 來知道說在做 XOR 的時候哪一些數字是會形成互相交換的群

# Methos1 - DP
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        record = [set() for _ in range(n)]
        record[0] = set([0])

        for row in range(m):
            for col in range(n):
                prev_record = record[col].union(record[col - 1]) if col else record[col]
                record[col] = set([grid[row][col] ^ v for v in prev_record])
        
        return min(record[-1])

# Method2 - Bit set swap
sm = (1 << (512)) - 1
swapmasks = [0]*9 + [sm]
for i in range(8, -1, -1):
    sm ^= sm << (1 << i)
    swapmasks[i] = sm

def swap_for(path, cell):
    for i in range(10):
        if cell & (1 << i):
            path = ((path & swapmasks[i]) << (1 << i)) | ((path & (swapmasks[i] << (1 << i))) >> (1 << i))
    return path

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        paths = [0]*n
        xor = grid[0][0]
        paths[0] = 1 << xor
        for c in range(1, n):
            xor ^= grid[0][c]
            paths[c] = 1 << xor
        xor = grid[0][0]
        for r in range(1, m):
            xor ^= grid[r][0]
            paths[0] = 1 << xor
            for c in range(1, n):
                paths[c] = swap_for(paths[c-1] | paths[c], grid[r][c])

        return (paths[n-1] & -paths[n-1]).bit_length() - 1

# Method3 - DFS
def dfs(idx, jdx, val):
    if 'out of boundary':
        'return None'
    if 'right bottom':
        'update_val'
        'return None'
    dfs(idx + 1, jdx, val ^ grid[idx][jdx])
    dfs(idx, jdx + 1, val XOR Gridvalue)
    
