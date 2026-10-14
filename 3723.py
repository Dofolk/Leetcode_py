# ===== Question =====
# 題目會給兩個數字 num 跟 sum(我自己改成 total，因為 sum 是內建函數名)
# 然後現在要找最大的一個數字字串滿足以下條件，可能會有多個滿足條件但要找最大
# 數字字串位數剛好是 num 位，然後每個位數加起來數字總和剛好是 total

# ===== Thoughts =====
# 這題要找最大值，然後有 num 個空位要填，可以採用 Greedy
# 每位位數只能填 0 ~ 9，要最大化的話就是盡可能讓 9 多一點並且往高位數去放
# 所以就可以去算 total 可以分出幾個 9，然後接著擺餘數，最後補 0 到 num 長度就可以了

# Method - Greedy
class Solution:
    def maxSumOfSquares(self, num: int, total: int) -> str:
        if total > num * 9:
            return ""
        q, r = divmod(total, 9)
        ans = "9" * q
        if r > 0:
            ans += str(r)
        return ans + "0" * (num - len(ans))
