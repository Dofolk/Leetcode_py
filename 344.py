# 這題是要將一個字串反著寫
# 做法就是將字串對半切，然後對於中間隊成的位置做交換
# 有個懶人解法，用 string.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        for i in range(L//2):
            s[i], s[L-i-1] = s[L-i-1], s[i]
