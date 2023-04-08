# 這題是給一個常對維 n 的整數字串，然後每次行動的時候可以對指定 n-1 個數字加 1，需要最少多少步可以讓所有數字都一樣
# 從數學上來想，假設 min 是最一開始數字串的最小值，sum 是最一開始的數字串總和，target 是最終相同的數值，m 則是從最一開始到最終目標所需行動的次數
# 從假設下，我們可以得到兩個等式
  # sum + m * (n-1) = target * n，因為可以知道說最一開始的和加上後面走的步數增加的數值一定會等於目標值乘上總長度
  # target = min + m，最小值如果要到目標的話一定就是要每次走的時候都要被加到
# 所以把第二式代入第一式的話就可以得到 m = sum - min * n，也就是最終結果

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)
