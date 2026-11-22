# ===== Question =====
# 給你一個只含 a 和 b 的字串，只要有任何 b 出現在某個 a 前面，就回傳 False，其餘情況回傳 True。

# ===== Thoughts =====
# 這題直接找最左邊的 a 跟最右邊的 b 之間的相對位置，直接比對就好
# 這題有個坑，少了 a 或 b 就是直接回傳 True

# Method - Directly Search
class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s or 'b' not in s:
            return True
        return s.rfind('a') < s.find('b')
