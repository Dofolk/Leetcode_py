# 這題是給一個字串，含有空白、數字跟英文字，然後把單字順序對調
# 做法就是用 split() 切開之後反過來 join 就可以回傳了

class Solution:
    def reverseWords(self, s: str) -> str:
        S = s.split()
        return " ".join(S[::-1])
