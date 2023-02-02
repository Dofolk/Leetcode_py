# 這題是給一個 list ，然後找出前 K 個出現頻率最高的數字是哪些
# 做法就是先用 counter 做計數，然後對出現次數做排序之後從 couter 裡面一個一個找符合次數出現的數字就可以了

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = collections.Counter(nums)
        ls = set(sorted(C.values())[-k:])
        res = list()
        for key in C:
            if C[key] in ls:
                res.append(key)
        return res
