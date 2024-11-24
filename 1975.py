# 這題是給一個方陣，裡面有正負數，你可以對任意相鄰(上下左右都可)的兩個位置做正負變換(就是乘上-1)，然後要算這個方陣經過這樣的操作後，最大方陣總數值合是多少
# 想法就是 greedy，我最貪婪的時候就是要全部都是正的，所以就遇到負數就全變成正數加起來，同時計算負數的數量
# 因為在給定的兩個任意位置，都可以透過相鄰乘-1的方式讓兩個位置作正負數變換，所以就記錄說負數有沒有偶數，偶數的話就可以全部都倆倆變換完畢
# 但是遇到奇數的話，就變得只剩下一個負數，這時候我們需要再另外紀錄一個最小值，用來解決這個問題
# 因為第三點的解釋，所以我們就可以來把這個最小值的地方做成負數，這樣扣起來會是傷害最小的，也就可以拿到最大的總和

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg = 0
        m = 1000000
        
        # go through the matrix values
        for i in matrix:
            for j in i:
                if j < 0:
                    j = -j
                    neg += 1
                if j < m:
                    m = j
                res += j
        # check the negative numbers, all negative numbers can transfer into positive if all negative number is even
        return res if neg%2 - 1 else res - m * 2
        
