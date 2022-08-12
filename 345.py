# 這題是要將字串的"母音"部分 reverse 就好
# 用 two pointer 來指向要交換的兩個位置
# 記得要先換成 list 才可以做，因為 str 的東西不能變更
# 最後回傳 list join 成 str 就好了

class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        p2 = len(s)-1
        T = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        while p1<p2:
            if s[p1] in T and s[p2] in T:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1
            elif s[p1] not in T and s[p2] not in T:
                p1 += 1
                p2 -= 1
            elif s[p1] not in T:
                p1 += 1
            elif s[p2] not in T:
                p2 -= 1
        return ''.join(s)
