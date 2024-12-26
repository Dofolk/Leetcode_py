# 這題是給一個數字 list 跟一個目標值 target，這邊只能使用 '+' '-' 來組成一個算式，問能達到目標值的算式有幾個？
# 背包 01 問題是選與不選，這題是必須選但是有兩個選項。以類似想法去操作，假設需要 '+' 的結果是 x，需要 '-' 的絕對值結果是 y，這樣我們的target = x - y
# 再加上 sum = x + y => x = (sum + target) // 2 ，所以就把題目要做的事情變成找看看所有數字有哪些組合可以得到 x ，採用 DP 操作
# 這邊還要先做一個預先處理，既然知道說要找的是 sum + target，所以可以測試 sum + target mod 2 有沒有餘數，理論上來說不應該有餘數出現
# 還可以確認一下說有沒有未達目標，全 '+' 或全 '-' 的情況下達不到目標也可以先刪掉了
# 在DP的第一步就是值為 0 的時候，是有 1 種方法可以填滿空間為 0 的背包，所以 DP 最一開始就是 1
# DP 的想法跟做法就是我從 target 往前去找，對於每個從 list 裡面出來的數字，從 target這個位置往前去找
# 代表著說我拿出來的這個屬字可以在哪幾個位置有作用，可以往前把之前的組合數量往後加上來

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)

        if S < abs(target) or (S + target) & 1: # if S < abs(target) or (S + target) % 2
            return 0

        target = (target + S)//2
        
        dp = [1] + [0] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[-1]
