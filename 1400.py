# 這題是給一個字串以及數字 k，問能不能用字串裡面的字元組出 k 個回文字串(不能重複使用)
# 做法就是有多少字元出現的次數是奇數個，比 k 小那就沒有問題
# 這樣的想法就是因為偶數個在處理回文的時候其實可以不用考慮，因為一定可以做出回文
# 但是當遇到奇數個的時候，一定會多一個字元出來，這個多出來的字元不一定能夠被處理好
# 所以在算的時候就是算說有多少個這樣多出來的字元(i.e. 出現奇數次的字元有幾個)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        odd_count = 0
        for char in set(s):
            if s.count(char) % 2:
                odd_count += 1
        return k >= odd_count
