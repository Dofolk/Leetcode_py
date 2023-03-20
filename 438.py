# 這題是給一個字串跟目標字串，然後去找哪些 index 往後的一段長度剛好是目標字串的 permutation
# 做法就是用先用一個字典存目標值，然後先做好整個字串的長度減一的檢測，把有遇到的字元先扣除掉，然後就開始做 slide window
# 移動視窗之後，先檢查看現在的位置有沒有在字典裡，有的話就加一，代表說已經要跑出去視窗外了
# 接著確認視窗尾端的是不是目標字串內的東西，是的話就減一
# 最後就要確認一下是不是每個字典的東西都是0，是就代表說這邊有個 permutation 並計數下來

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL:
            return res
        
        for ch in p:
            hm[ch] += 1
        for i in range(pL - 1):
            if s[i] in hm:
                hm[s[i]] -= 1
        for i in range(-1, sL - pL + 1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i + pL < sL and s[i + pL] in hm:
                hm[s[i + pL]] -= 1
            if all(v == 0 for v in hm.values()):
                res.append(i + 1)
        return res
