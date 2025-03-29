# === Description ===
# 給一個大小為 m x n 的整數矩陣 grid 和一個大小為 k 的陣列 queries，對每個 queries[i] 進行操作，並計算得到一個大小為 k 的陣列 answer
# 對於每個 queries[index]，可以操作: 從矩陣的左上角開始
# 如果 queries[i] > 當前格子的數值，你會得到 1 分，並且可以移動到相鄰的任何一個格子（上下左右四個方向）。
# 如果 queries[i] <= 當前格子的數值，則無法獲得任何分數，並結束該次操作。
# 最後，answer[i] 是你在這個過程中能獲得的最大分數。需要注意的是，你可以多次拜訪同一個格子。
# 簡單來說，就是對每個 queries[i]，從左上角出發，根據矩陣的數值進行移動，並嘗試獲得最多的分數，最終返回每次查詢對應的最大得分。

# === Thought ===
# 這題的想法就是先對 queries 裡面的數字及位置(index)做對應，接著依照數字大小從小排到大
# 接著就可以在 grid 做 BFS 來搜尋路徑，只是這邊在跑路徑的時候是用 heap 來操作，目的就是讓所有能跑到的小數字都先跑完
# 然後這邊就把跑過的數字改成 0 來避免重複計算的問題，所以在跑的時候也要確認數字有沒有存在
# 還有在找下一步的時候也適用 heappush 來操作，讓越小的數字可以盡早被跑到過
# 用 accumulate_points 來記錄說目前跑幾個數字了，如果跑的時候遇到發現 queries 的數字比較小的時候，就把結果記錄下來
# 等所有數字都比對過之後就可以回傳了

# === Code ===
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row, col = len(grid), len(grid[0])
        res = [0] * len(queries)

        accumulate_points = 0
        heap = [(grid[0][0], 0, 0)]
        grid[0][0] = 0
        
        for query_idx, query_value in sorted(enumerate(queries), key = lambda x: x[1]):
            while heap and heap[0][0] < query_value:
                _, current_row, current_col = heappop(heap)
                accumulate_points += 1
                for dx, dy in directions:
                    new_row, new_col = current_row + dx, current_col + dy
                    if new_row >= 0 and new_col >= 0 and new_row < row and new_col < col and grid[new_row][new_col]:
                        heappush(heap, (grid[new_row][new_col], new_row, new_col))
                        grid[new_row][new_col] = 0
            res[query_idx] = accumulate_points
        return res
