# 這題是給一個數目總額跟硬幣池(各個硬幣數量無限)，然後要問有幾總方法可以湊出目標數目
# 做法是 DP，對於每一種硬幣做等間隔相加，例如：5元面額的就是每個5個間隔去相加
# dp 這個 list 就是存目前每個數目有幾種加總方法，所以最一開始只有 0 有 1，剩下都是 0
# 然後就逐個往後疊加就可以了

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for val in range(coin, amount + 1):
                dp[val] += dp[val - coin]
        
        return dp[-1]


