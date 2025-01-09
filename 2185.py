# 這題是給一個字串 list 跟一個開頭的字串 pref，問 list 裡面有多少字串是 pref 開頭的
# 如果是開頭的就回傳 1，不是就回傳 0，最後再加總起來就好了

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 if word.startswith(pref) else 0 for word in words])
