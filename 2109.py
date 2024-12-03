# 這題是給一個字串跟需要空白的位置，將空白插入其中並回傳字串
# 做法就是從空白位置做迴圈，這樣可以讓迴圈跑的次數最少，這樣就可以把字串給切成一段一段的，最後在用 join() 來做字串的合併

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ls = []
        idx = 0
        for space in spaces:
            ls.append(s[idx:space])
            idx = space
        ls.append(s[idx:])
        return ' '.join(ls)
