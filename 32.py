# ===== Question =====
# 題目給一個只有左右括號 () 的字串，然後算最長的合法子字串多長

# ===== Thoughts =====
# 組成合法 () 的時候可以考慮用 stack 來操作，要找最長所以需要有連續型的想法在
# 連續型的想法可以用遇到合法組合就更新位置及答案來操作
# stack 來記錄遇到的 ( 位置在哪以及前一次的 ) 在哪裡，然後遇到 ) 的時候就可以去更新長度
# 更新的方法就是遇到 ) 就把 stack 給 pop 掉，代表我把前一個 ( 或 ) 的位置移除
# ( 就是配對掉所以移除掉，) 就是來更新上次位置的
# 代表我可以從上次的 ) 或是前面的 ( 一直計算到現在當下的位置
# 所以最後直接去 max 答案跟 stack 最後的位置就可以了

# Method - Stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            else:
                stack.pop()
                
                if not stack:
                    stack.append(idx)
                else:
                    ans = max(ans, idx - stack[-1])
        
        return ans
