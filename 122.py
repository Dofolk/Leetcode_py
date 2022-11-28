# 這題是要找股票買賣的時機，找出最大的獲利
# 買賣不限一次，所以想法就是所有遞增的就給他全部都加起來就對了

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        M = 0

        for i in range(1,len(prices)):                
            if prices[i]<=prices[i-1]:
                M += prices[i-1] - prices[p1]
                p1 = i
        
        M += (prices[-1]-prices[p1]+abs(prices[-1]-prices[p1]))//2

        return M
      
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        M = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                M += prices[i]-prices[i-1]
        return M
