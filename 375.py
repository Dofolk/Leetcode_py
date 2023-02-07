# 這題是要玩猜數字遊戲，猜 x 猜錯時要付 x 元，然後給定一個數字 n，找看看最少用多少錢可以猜到數字(這邊題目寫得有點怪怪的，有可能會誤會成最多多少錢)
# 做法就是考慮間隔數的花費之後再去下做 DP，因為我可以透過間隔的去猜數字來達到最好的效益
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/solutions/1510747/python-dp-beat-97-52-in-time-99-in-memory-with-explanation/

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        start_idx = 1 if not n%2 else 2
        select_num = [i for i in range(start_idx, n, 2)]
        select_num_len = len(select_num)
        dp = [[0] * select_num_len for _ in range(select_num_len)]
        
        for i in range(select_num_len):
            dp[i][i] = select_num[i]

        for length in range(2, select_num_len + 1):
            for i in range(select_num_len - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j + 1):
                    dp_left = dp[i][k - 1] if k != 0 else 0
                    dp_right = dp[k + 1][j] if k != j else 0
                    dp[i][j] = min(dp[i][j], select_num[k] + max(dp_left, dp_right))

        return dp[0][-1]
