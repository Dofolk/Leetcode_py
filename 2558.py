# 這題是給一個數字 list，然後每次操作都對其最大數字開平方根並且向下取整，經過 k 次操作之後，問最後 list 總和多少
# 做法就是先將給定的 list 都加上負號做成 heap，這樣就有 max heap 了，接下來對其操作 k 次取出、加負開根號之後，再加負放回去
# 最後回傳負的加總就大功告成了
# note: heap 用來加快速度的

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ls = [-i for i in gifts]
        heapq.heapify(ls)
        for _ in range(k):
            M = heapq.heappop(ls)
            heapq.heappush(ls, -math.floor((-M) ** 0.5))
        return -sum(ls)
