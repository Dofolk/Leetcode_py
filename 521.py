# 這題是要找最長的不相等子字串
# 基本上這題除了完全相等的兩個字串之外，剩下都是不相等的
# 所以這題就是去比看字串有沒有完全相似，有的話就回傳 -1，沒有的話就回傳最長的字串長度

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        L1, L2 = len(a), len(b)
        M = max(L1, L2)
        if L1 == L2:
            for i in range(L1):
                if a[i] != b[i]:
                    return M
                if i == L1-1 and a[i]==b[i]:
                    return -1
        return M
