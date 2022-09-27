# 這題是要把字串做分類，有相同字母組成的分成一類
# 做法就是用 dict 來記錄看過的值，然後對每個字做 sorted 以確保組成字母的一致性
# 所以遇到一樣組成的就在對應的 list 加字串進去，最後就回傳 dict().values()的 list 就可以了

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for i in strs:
            sort_str = ''.join(sorted(i))
            if sort_str in D:
                D[sort_str].append(i)
            else:
                D[sort_str] = [i]
        
        return list(D.values())
