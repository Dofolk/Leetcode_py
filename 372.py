# 這題是給數字 a 跟數字 list b(一位數表示，[1,2,3]=123)，然後要找a^b mod 1337是多少
# 用 Euler's Theorem，找到 1140

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return (a % 1337) ** ( 1140 + int(''.join(map(str, b))) % 1140 ) % 1337
