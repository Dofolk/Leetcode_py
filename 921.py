# ===== Question =====
# 題目給一個只有 () 的字串，然後問最少總共要補幾個 ( 或 ) 才能讓字串合法
# Note: 題目設定是 Med，但實際難度是 easy

# ===== Thoughts =====
# 這題一樣就是去做括號配對，可以用 stack 存目前有看到的 ( 起來，然後遇到 ) 的時候就減掉一個
# 然後如果 stack 是空的沒有 ( 的時候就是一定得要補了，這邊就變成在 answer 的數量 +1
# 最後再確認整個字串到最後還有幾個 ( 就需要補相對應數量的 ) 來完成合法組合
# 這邊可以用一個 count 來取代 stack 的功用，計算當下位置前有幾個左括號
# 遇到左括號就 count + 1，遇到右括號就 - 1 或是補左括號讓 ans + 1
# 最後再把 ans 跟 count 加起來就可以補完餘下的左括號了

# Method - Count
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        left_count = 0

        for c in s:
            if c == '(':
                left_count += 1
            else:
                if left_count:
                    left_count -= 1
                else:
                    ans += 1
        
        return ans + left_count
