# 這題是給一個逆波蘭表示法(RPN)的序列，然後把值算出來
# 做法就是用 stack 來存遇到的值，當遇到運算符號時就把最近遇到的兩個值叫出來計算，算完後丟回去 stack 裡面等之後的操作
# 然後用一個 dict 來存遇到運算子時要做哪些東西，用 lambda 來宣告簡單的運算


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = list()
        m = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : int(x/y)
        }

        for t in tokens:
            if t in m:
                b = s.pop()
                a = s.pop()
                s.append(m[t](a,b))
            else:
                s.append(int(t))
        return s[0]
