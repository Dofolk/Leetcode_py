# ===== Question =====
# 題目給一個數字 n 代表直線上有編號 0 ~ n - 1 個點以及一個常數 k，求不相交線段恰好有k條時的組合有幾個
# 端點重合不算相交，以不要求所有點都一定要被覆蓋
# ex. n = 4, k = 2，代表現在要在 0 ~ 3 這 4 個點找出恰好兩個不相交線段，總共 5 種組合
# {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}

# ===== Thoughts =====
# 想法有二，一個是dp，一個是數學組合計算

# dp 的想法比較直接，假設要找點 [0, j] 這個點區間要有 i 個線段時，遞迴算是如下
# dp[i][j] = dp[i][j - 1] + sum_{p = 0}^{j} dp[i - 1][p]
# 這邊可以看到有個 sum over past，如果直接把這部分每次遞迴都算的話時間最高有可能要到 n^3
# 所以這部分可以用一個 prefix 來記錄 sum over past 的部分
# 接著就是 dp 的部分可以觀察到大多數變動的時候都是 i 的部分，所以這部分可以用 rolling dp 來最佳化空間利用

# 另一個想法就是組合的概念
# 線段是由兩個點組成的，所以總共 n 個點要取 2 * k 個點出來剛好就可以組成 k 個線段
# 但是這邊會有問題是端點重合不算相交，但是在取點的時候卻是可以重複取點，所以有重複點的case會沒辦法選取到
# 所以這邊可以做一個 1-1 的函數把選取的點區分開來，這樣就可以精確的選取到重複點了
# 這個函數的設計就是把選定的左右端點根據他被選取的順序(idx)往右移動 idx - 1 格
# f:(left_i, right_i) -> (left_i + idx - 1, right_i + idx - 1)
# 這樣選取的範圍就從 0 ~ n - 1 變成 0 ~ n - k + 1，所以組合的選就是 C (n + k - 1) 取 2k

# Method 1 - DP
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * n
        prefix = [0] * (n + 1)
        
        for jdx in range(n):
            prefix[jdx + 1] = (prefix[jdx] + dp[jdx]) % MOD
        
        for _ in range(k):
            dp[0] = 0

            for jdx in range(1, n):
                dp[jdx] = (dp[jdx - 1] + prefix[jdx]) % MOD
            
            for jdx in range(n):
                prefix[jdx + 1] = (prefix[jdx] + dp[jdx]) % MOD
        
        return dp[n - 1]


# Method2 - Combinations
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % (10 ** 9 + 7)
