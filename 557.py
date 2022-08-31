# 給定一個字串，以一個空白當分隔，將分隔開來的字串逐個做反轉，只反轉單獨字串，不要整個大字串反轉
# 做法就是用 split() 先分割好小字串，然後逐個用 s[::-1] 做相加並加上空白，最後回傳的時候就不要回傳到最後一個空白就好

class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split()
        ans = str()
        for i in S:
            ans += i[::-1]
            ans += ' '
        return ans[:-1]
