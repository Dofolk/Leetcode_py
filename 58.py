class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = len(s)
        L1 = 0
        for i in range(L-1,-1,-1):
            if (s[i]!=" ") and (L1==0):
                L1 += 1
                continue
            if (s[i]==" ") and (L1!=0):
                break
            if (s[i]!=" ") and (L1!=0):
                L1 +=1
        return L1
      
# 從字串尾端開始找word
# 第一次用空白來找word有bug，遇到單一字元就炸掉了
# 也可以用while來做：
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = len(s)
        L1 = 0
        while L>0:
            L -= 1
            if s[L]!=" ":
                L1 += 1
            elif L1 > 0:
                return L1
        return L1
'''
