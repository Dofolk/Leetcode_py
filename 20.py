class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { "}":"{" , ")":"(" , "]":"[" }
        
        for t in s:
            if t in mapping:
                top = stack.pop() if stack else '#'
                if (mapping[t] != top):
                    return False
            else:
                stack.append(t)
        return not stack
      
# 因為括號是成對的，所以遇到右括號的時候前面一定要是跟自己成對的
# 想法：建立一個list來儲存最近一個左括號是哪一個，遇到右括號的時候再拿出來比對跟return
# 所以就把整個括號的string跑一遍，遇到右括號就pop list的值出來比對跟return，遇到左括號就把左括號加進去list
# 最後，list裡面如果都有pop出來的話就是空的list(相當於否定)，所以return '否定list' 的結果
