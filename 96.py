# 這題是要算看看 1~n 的數字做成二元搜尋樹(BST)有幾種可能性
# 想法就是來算左右子樹的數量，左右子樹可能的數量相乘就會是該 root 的可能性
# 所以第一個 for 就是來看看要算幾個數字的，第二個 for 就是開始計算左右子樹的數量後相加

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]
