# 這題是給兩個字串 str1 跟 str2，然後有個規矩是可以對str1的字母做一次的循環遞增位移，就是 a 可以變成 b，z 可以變成 a
# 在這樣的狀況下，str2 能不能是 str1 的 subsequence
# 做法就是對 str1 跑一遍迴圈，然後用一個指標 idx 來記錄 str2 的位置，如果字母一樣或是可以遞增位移的話就 idx + 1
# 最後回傳 idx 有沒有跟 str2 的長度一樣就好

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        idx, L = 0, len(str2)
        for c in str1:
            if idx < L and (ord(str2[idx]) - ord(c)) % 26 < 2:
                idx += 1
        return idx == L

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        D = dict()
        for i in range(26):
            D[chr(i + 97)] = i
        idx, L = 0, len(str2)
        for i in range(len(str1)):
            if str1[i] == str2[idx] or (D[str1[i]] + 1) % 26 == D[str2[idx]]:
                idx += 1
                if idx == L:
                    return True
        return False
        
