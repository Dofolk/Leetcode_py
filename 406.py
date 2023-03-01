# 這題是給一個列表，列表會有身高跟前面有多少人高>=自己的數量，然後要把順序改一下，變成按照人數下去排，然後再排身高
# 做法就是用 sort 先排出身高順序，從高的往矮的去逐個排序

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:(-x[0],x[1]) )
        res = []
        for p in people:
            res.insert(p[1],p)
        return res
