# 這題是給一串 citation 的數量，然後找 h-index(有n篇被引用了n次以上，他的H指數是n)
# 作法有2個，簡單點就是先排序然後從尾端開始往前找
# 另一種做法是用 bucket sort 的概念，統計一下各個 cite 的數量有幾篇，然後一樣從尾端往前加總

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        bucket = [0] * (L+1)
        
        for v in citations:
            if v >= L: bucket[L] += 1
            else: bucket[v] += 1
        
        i, h = L, 0
        while i >= 0:
            h += bucket[i]
            if h >= i: return i
            i -= 1
        return h
      
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        citations.sort()
        h = 0
        for i in range(1, L+1, 1):
            if citations[L-i] < i:
                return h
            else:
                h += 1
        return h
