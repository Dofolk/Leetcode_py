# 這題是給一個字串，然後按照順序把字母做倍數增長並回傳，EX: 2[a3[c]]3[b] => acccacccbbb
# 做法就是一個 stack 來存目前遇到的東西，當遇到 ] 時就把東西拿出來，看那些字母要成幾倍
# 中間都用 while 來擷取出 stack 裡面的東西

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == ']':
                tmp = stack.pop()
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                multi = stack.pop()
                while stack and stack[-1].isdigit():
                    multi = stack.pop() + multi
                stack.append(tmp * int(multi))
            else:
                stack.append(c)
        return ''.join(stack)
