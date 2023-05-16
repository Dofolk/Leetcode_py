# 這題是給一個字串集，每個字串由 0 1 構成，然後給 m n 兩個數字表示 0 1 的需求，然後要去找這樣的需求之下可以最長可以拿到多大的子集
# 做法就是用 DP，用一個矩陣來存最長可以得到多長，想法就是現在這個字串我拿著時我要選擇他或是捨棄掉，哪個可以有比較長的子集
# 先從給定的字串集一個一個拿出來找，計算字串的 01 數量
# 然後從最後面往前去找，固定往前 zeros 跟 ones，代表就是在每個狀況下選擇了這個字串的話可以拿到最長多少的子集

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [ [0] * (n+1) for _ in range(m+1) ]
        
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
        
        return dp[-1][-1]
