# 這題是給一個 array，裡面有標點 0 跟 1，1 代表有 server 在，0 則是代表沒東西在，現在 server 在同一條 row 或 col 時可以互相聯絡
# 問說整個網路途中，最多有幾台電腦是可以互相聯絡的
# 想法就是我以 row 為出發點，先檢查每個 row 有沒有超過1 台的 server，有就紀錄數量，代表這條 row 有這麼多台 server 可以互相聯絡
# 接下來是，如果遇到 row 裡面只有一台電腦的時候，就要去確認說 col 的數量
# 如果那個 col 有超過一台電腦的話，我就可以把這個 row 上的這台電腦紀錄下來，因為他在 col 上也是可以有互相聯絡的
# 如果是沒有辦台 server 的話就可以不理它了，直接跳到下一條 row 去
# 最後回傳紀錄的數量就好了

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for idx in range(m):
            S = sum(grid[idx])
            if S > 1:
                ans += S
            elif S == 1:
                col = grid[idx].index(1)
                if sum([grid[i][col] for i in range(m)]) > 1:
                    ans += 1
        return ans
