class Solution:

# 基本上就是都尋訪一遍
# 第一個方法就是two pointer，根據跑的位置就慢慢找區間的最大利益
# 第二個方法有個基本概念，就是當價格比前一天低可以想成一波可以更新檔期的時候，再來看看需不需要更新，反正存好最低點我就找後面最高點賣就好了

  
# Solution 1
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for i in range(len(prices)):
            p = prices[i]-minprice
            if p<0:
                minprice = prices[i]
            elif p>profit:
                profit = p
        return profit
      
# Solution 2
      def maxProfit(self, prices: List[int]) -> int:
        m = 0
        left = 0
        right = 1
        l = len(prices)
        while right<l:
            profit = prices[right] - prices[left]
            if profit>=0:
                m = max(m,profit)
            else:
                left = right
            right += 1
        
        return m
