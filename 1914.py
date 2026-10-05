# ===== Question =====
# 題目給一個 m x n 的 2d array grid 以及一個數字 k，然後最外面圍成一圈開始逆時針旋轉 k 步
# 傳完之後往內一圈一樣走 k 步的流程，一直重複步驟直到最內圈
# 另外限制說 m 跟 n 一定是偶數，所以不會發生奇數寬度或長度的陣列要做逆時針旋轉

# ===== Thoughts =====
# 這題直接實際操作位置就可以了，做法就是洋蔥式跑法，一層跑完再往下跑下一層
# 首先先找出長寬哪邊比較短，把短邊除 2 就知道說要跑得圈數
# 接著每一圈都去紀錄每一圈的 row idx, col idx, element value
# 這邊使用三個 list 去分別記錄上面的這些數值，紀錄的時候就一樣按照逆時針方向開始記錄
# 首先先從左邊的 column 紀錄，接著記錄最底下的 row，沿著右邊 column 往上之後接回倒敘的最上層 row
# 這樣就沿著一圈遍歷一遍了，然後根據總長度去計算每一個數值對應到的位置在哪裡
# 這時候只要去動 element value 的 index 就好，讓他跑到對應的位置之後抓對應的 row idx, col idx
# 最後再把 grid[row idx][col idx] 的數值改成現在的 element value 就可以了

# Method - Stack
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        cycles = min(m, n) // 2

        for cycle in range(cycles):
            row = [] # store the row index
            col = [] # store the column index
            val = [] # store the corresponding values

            # Left column value storage
            for r in range(cycle, m - cycle - 1):
                row.append(r)
                col.append(cycle)
                val.append(grid[r][cycle])

            # Bottom row value storage
            for c in range(cycle, n - cycle - 1):
                row.append(m - cycle - 1)
                col.append(c)
                val.append(grid[m - cycle - 1][c])

            # Right column value storage
            for r in range(m - cycle - 1, cycle, -1):
                row.append(r)
                col.append(n - cycle - 1)
                val.append(grid[r][n - cycle - 1])

            # Top row value storage
            for c in range(n - cycle - 1, cycle, -1):
                row.append(cycle)
                col.append(c)
                val.append(grid[cycle][c])

            # Check the current cycle length and the step length by k
            cycle_len = len(row)
            step = k % cycle_len
            for idx in range(cycle_len):
                # idx_after: the index after rotating with 'step' steps
                idx_after = (idx - step) % cycle_len
                # The value of current grid position will be changed as the value after rotating 
                grid[row[idx]][col[idx]] = val[idx_after]

        return grid


from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        cycles = min(m, n) // 2

        for cycle in range(cycles):

            top = cycle
            bottom = m - 1 - cycle
            left = cycle
            right = n - 1 - cycle

            val = []  # store the corresponding values

            # Top row value storage
            for c in range(left, right + 1):
                val.append(grid[top][c])

            # Right column value storage
            for r in range(top + 1, bottom + 1):
                val.append(grid[r][right])

            # Bottom row value storage
            for c in range(right - 1, left - 1, -1):
                val.append(grid[bottom][c])

            # Left column value storage
            for r in range(bottom - 1, top, -1):
                val.append(grid[r][left])

            # Check the current cycle length and the step length by k
            cycle_len = len(val)
            step = k % cycle_len
            # Rotate the cycle values with 'step' steps
            val = val[step:] + val[:step]

            idx = 0
            # The value of current grid position will be changed as the value after rotating
            # Top row value update
            for c in range(left, right + 1):
                grid[top][c] = val[idx]
                idx += 1

            # Right column value update
            for r in range(top + 1, bottom + 1):
                grid[r][right] = val[idx]
                idx += 1

            # Bottom row value update
            for c in range(right - 1, left - 1, -1):
                grid[bottom][c] = val[idx]
                idx += 1

            # Left column value update
            for r in range(bottom - 1, top, -1):
                grid[r][left] = val[idx]
                idx += 1

        return grid
