# 這題是要去算 <= 給定值的質數有多少個
# 做法就是先假設全部都是質數，然後把0, 1變成非質數，接著就開始做 for loop
# 把遇到的 i^2 一直到底，每間隔 i 個數字就是非質數(因為可以被整除)
# 最後去加總就可以得到質數數量了
# 這邊有先做偶數的替換，減少 For 裡面的操作次數

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        dp = [1] * n
        dp[0] = dp[1] = 0
        dp[4::2] = [0] * len(dp[4::2])
        for i in range(3, ceil(n**0.5), 2):
            if dp[i]:
                dp[i*i::i] = [0] * len(dp[i*i::i])
        return sum(dp)
