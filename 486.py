# 這題是給一個數字列表，然後兩個人每次只能選頭或尾的數字，最後看看總和大小誰贏
# 做法就是從最小列表一直加到大列表， DP 的概念用在根據上一次的數字和以及新加進來的數字，作一些相減得到結果
# 現在就都站在 P1 的角度上來看待數字，所以如果最後結果 >0 就代表能贏

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i]-dp[j], nums[j] - dp[j - 1])
        
        return dp[-1] >= 0
