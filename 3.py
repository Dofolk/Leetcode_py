# 這題是要找看看字串中"最長的不重複子字串長度"是多少
# 作法就是用 two pointer 來做，後面的指標如果找到重複的字的話就更新前面指標的位置

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        p1, p2, M = 0, 1, 1
        while p2 < len(s) and p1 < len(s):
            if s[p2] not in s[p1:p2]:
                p2 += 1
                M = max(M,p2-p1)
            else:
                p1 += 1
        return M
