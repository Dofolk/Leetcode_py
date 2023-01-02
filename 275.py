# 這題跟274一樣要找 citation 的 h-index，差別在這題給的是已經排序好的
# 簡單做法就是直接 for 下去跑，比274少了一個 sort 的指令
# 另一個做法就是用 binary search 的想法，找出中間值在哪裡，然後回傳 總長度-中間值 就可以了

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r, L = 0, len(citations) - 1, len(citations)

        while l <= r:
            m = (l + r) // 2
            if citations[m] >= L - m:
                r = m - 1
            else:
                l = m + 1
        return L - l
      
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        h = 0
        for i in range(1, L+1, 1):
            if citations[L-i] <= h: return h
            else: h += 1
        return h
