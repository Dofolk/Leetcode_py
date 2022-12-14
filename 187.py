# 這題是給一串 DNA，然後找裡面有重複出現的字串
# 做法就是用一個 set 來存看過的字串，再次遇到就把該字串存到結果裡

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10: return []
        res, rec = set(), set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in rec: res.add(sub)
            else: rec.add(sub)
        return list(res)
