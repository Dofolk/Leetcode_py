# 這題是在找有沒有 subsequence
# 用 two pointer 做，當 sequence 的 pointer跑到最後兒還沒找完 subsequence 的話就回報錯誤

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1<len(s):
            while p2>=0:
                if p2 == len(t):
                    return False
                elif s[p1]==t[p2]:
                    p2 += 1
                    break
                else:
                    p2+=1
            p1 += 1
        return True
