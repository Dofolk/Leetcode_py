# 這題是給一個 2 x n 的 array，然後從 (0, 0) 走到 (2, n - 1)
# 首先第一台機器人會把走過的所有數字都吃掉，並且想讓第二台機器人盡可能地減少它所能吃的數字加總
# 而第二個機器人就是得要在地一台機器人走過之後，盡量吃掉最大的數字加總
# 想法就是第一台會走一個轉彎，到第二條 row 上，所以這樣的話可以找從哪個點做轉彎可以最大的減少
# 所以先做 suffix 來看看第二台機器人第一條 row 後面剩餘的數字總和能吃多少
# 或是 prefix 來看看第二條 row 前面總和能吃多少
# 接著就逐步去做 prefix 加總跟 suffix 的減少
# 對於每個位置都去比較數字的大小，取得第二台機器人最多能吃的總賀數值最小的那個( min(max) )

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix, suffix = 0, sum(grid[0][1:])
        ans = max(prefix, suffix)
        for idx in range(len(grid[0]) - 1):
            prefix += grid[1][idx]
            suffix -= grid[0][idx + 1]
            M = max(prefix, suffix)
            if M < ans:
                ans = M
            else:
                break
        return ans
