# 這題會給一堆類型的糖果，每個數字代表不同類型的糖果，可以想成是不同口味的糖果，然後現在只吃一半的糖果，最大化吃到的口味
# 作法很簡單，先把糖果變成 set() 就可以知道有幾個口味，然後再看看口味的數量跟總數的一半那個比較少就對了

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)),len(candyType)//2)
