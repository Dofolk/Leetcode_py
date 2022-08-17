# 這題是找看看給定的字串能做出最常多長的回文字串
# 因為回文，所以就確認每個字元出現 >=2 次的次數，然後就可以除以2來算半段回文長度

class Solution:
    def longestPalindrome(self, s: str) -> int:
        single = 0
        length = 0
        ls = set(s)
        for i in ls:
            c = s.count(i)
            if c == 1:
                single = 1
            if c >= 2 and c%2:
                single = 1
                length += c//2
            elif c >= 2:
                length += c//2
        return 2*length+single
