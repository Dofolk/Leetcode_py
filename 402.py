# 這題是給一個數字字串，然後要移除 k 個字元，讓剩下的數字會最小，問最小值是多少
# 做法就是先缺任長度，全部都移除光就是直接歸零
# 然後依照順序，如果前一個數字比後一個還大的話就把前一個數字刪掉，因為遞增的數列會讓數字更大
# 實現的方法就是用 stack 來存遇到的數字，並且不要空 stack 存到 0 (因為就沒有東西了)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        L = len(num)
        if L <= k:
            return '0'
        stack = []

        for n in num:
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1
            if stack or n is not '0':
                stack.append(n)

        if k:
            stack = stack[0:-k]
        
        return ''.join(stack) if stack else '0'
