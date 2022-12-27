# 這題是給一個數字運算是的字串，然後算出它的結果來
# 做法是用類似stack的作法，把前一個的結果先暫存起來，當下如果是 + 或 - 就把前個結果加進 res 裡，如果不是的話就把前個結果做 */

class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        res, prev, cur = 0, 0, 0 # res紀錄所有結果，prev紀錄前一個區塊的計算結果(+-之間的，因為*/要先算所以把*/看成是一串連續運算的區塊)，cur紀錄當下拿到的數字是多少
        sign = '+' # 紀錄最近一個遇到的運算符號是啥，根據這個運算符號來決定當下步驟要做甚麼
        s += '+' #最後把cur的結果往前推進一個新的區塊
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c) #
            elif c.isspace():
                continue
            elif c in '+-*/':
                if sign == '+':
                    res += prev
                    prev = cur
                elif sign == '-':
                    res += prev
                    prev = -cur
                elif sign == '*':
                    prev *= cur
                elif sign == '/':
                    prev = int(prev/cur)
                sign = c
                cur = 0
        return res+prev

# 也可以用 stack 來做，用 stack 來存計算完的數字，-就是負號，遇到 */ 就坐運算，遇到+-就把值往裡面塞
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        stack, num, sign = list(), 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + ord(s[i]) - ord('0')
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append( stack.pop() * num )
                else:
                    tmp = stack.pop()
                    v = tmp//num
                    if v<0 and tmp%num!=0:
                        stack.append(v+1)
                    else: stack.append(v)
                sign = s[i]
                num = 0
            
        return sum(stack)
