# 這題是要看看 ransomNote 的字母能不能由 magazine 裡的字元組合起來，而且 magazine 的字元不能重複使用
# 所以就是用 in 來看有沒有存在，不存在就回報錯，存在就把 magazine 的字元移除掉(因為不能重複使用)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ls = list(magazine)
        for i in ransomNote:
            if i not in ls:
                return False
            else:
                ls.remove(i)
        return True
