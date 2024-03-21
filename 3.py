# 這題是要找看看字串中"最長的不重複子字串長度"是多少
# 作法就是用 two pointer 來做，p1在前，p2在後
# 讓p2開始跑並更新最大值，直到p2只到p1~p2區間內重複的字之後就來更新p1的位置，讓字母不重複
# 一直持續上面步驟直到 p1 p2 都跑到底就知道最長是多少了

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
