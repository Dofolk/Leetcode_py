# 這題是要設計一個 class 來找第 k 個最大的數字是多少
# 一開始的 init 是先把 list 變成 heap 的形式，然後開始丟東西出來到長度是需要的長度
# 然後就開始在 heap 裡面加東西進去，還要再確認一下有沒有超過長杜，有的話一樣就開始丟東西出來直到長度符合

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
