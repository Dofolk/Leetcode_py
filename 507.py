# 這題是要看近來的數字是不是完全數
# 因為數字很少，直接列出來

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        N = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]
        return num in N
