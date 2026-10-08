# ===== Question =====
# 題目給一個合法的 ()字串，然後要回傳把最外層 () 移除之後的結果
# ex: (()()) => ()(), (())(((()))()) => ()((()))()

# ===== Thoughts =====
# 這題簡單來說就是要把深度為 0 的括號組去掉，題目也確定會給一個合法的括號組字串了
# 所以這題就可以直接操作，計算目前的括號組深度是多少，根據深度看要不要存就可以了
# 所以先宣告一個 list 存 result，然後一個 count 來算深度
# 迴圈裡面確認是左還右括號，嘬括號就先確認深度之後再把深度 + 1，右括號則是順序相反
# 這樣才會符合正確的深度計算

# Method 1 - Bracket Depth Count
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        count = 0

        for c in s:
            if c == '(':
                if count > 0:
                    res.append(c)
                count += 1
            else:
                count -= 1
                if count > 0:
                    res.append(c)
        
        return ''.join(res)
