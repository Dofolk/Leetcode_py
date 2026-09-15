# ===== Question =====
# 題目給一個字母字串 s 以及一個常數 k，求非重疊且長度至少為 k 的回文子字串(連續)最多能有幾個
# ex. s = "abaccdbbd", k = 3: aba 跟 dbbd 兩個

# ===== Thoughts =====
# 可以用 greedy 的方法來想 Time: O(nk)
# 要最大化字串數量就是把長度最小化，所以就考慮長度為 k 以及 k + 1 的兩個子字串
# 因為不重疊，所以一個回文字串不管是取權長度還是取中間一小段都只能取一次
# 在選取的時候就不要用全長度的選取，因為會不知道全長度是多長
# 所以這邊就直接選中間的那一段就好了，反正只能取一次
# 接著就開始針對 k 及 k + 1 兩種長度遍歷一次全部 s 就可以了

# 另外也可以用 dp 來想 Time: O(n^2)
# dp 的想法就比較簡單，透過一個 2d 陣列(pal[left][right])來記錄 left 到 right 這段有沒有回文(True False)
# 首先就先把所有子字串長度都跑過一遍來更新這個 dp 陣列
# 更新方法就是檢查 左右兩個字元要一樣 以及 進一步縮短距離也要回文or長度<=2(這樣才能回文)
# 接著拉一個 dp 來用，遍歷每個字元，然後從該字元往前長度至少 k 的這個區間段(index j ~ index i)是不是回文
# 如果是的話就更新 dp，確認當前的位置(index i)數值大還是前一步(index j)多算這一個新的回文

# Method 1 - Greedy
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        ans = 0
        last = 0

        for right in range(k - 1, len(s)):
            left = right - k + 1
            if left >= last and check(left, right):
                ans += 1
                last = right + 1
                continue
            left = right - k
            if left >= last and check(left, right):
                ans += 1
                last = right + 1
        
        return ans


# Method2 - DP
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                is_palindrome[left][right] = (s[left] == s[right]) and (
                    length <= 2 or is_palindrome[left + 1][right - 1]
                )

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if is_palindrome[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]
