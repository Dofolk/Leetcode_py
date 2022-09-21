# 這題是給一個數字，然後做出合法的，等量的 () 組合並列出來
# 做法是用遞迴來操作，當長度為 2n 時就是要把東西存起來了，然後就開始看左右括號的數量來看要怎麼補
# 如果左括號的數量不到 n，那就補左括號直到有 n 個左括號，然後就開始補右括號直到滿
# 接下來就是把右括號移除，再多移除一個左括號，然後補上右括號之後再開始補左右括號直到長度足夠
# 透過這方是一層一層慢慢分離，建構出所有的可能性

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()
        
        backtrack([], 0, 0)
        return ans
