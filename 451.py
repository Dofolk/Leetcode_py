# 這題是給一個字串，然後依照出現的次數重新排列
# 作法就是先用 Counter 算次數然後做一次排序，排好之後按照順序一個一個加起來就好了


from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        C = Counter(s)
        res = str()
        for char, n in C.most_common():
            res += char * n
        return res
