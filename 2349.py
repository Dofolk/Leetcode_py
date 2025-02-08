# 這題是要設計一個 class， change 可以把 index 的數字換成 number， find 就是要去找給定的 number 出現在最小的 index 是哪個
# 因為有扯到最小所以考慮用 heap，首先先用兩個字典 index_number 跟 index_list 分別來存 index 目前的數值以及 number 有出現過在哪幾個 index 過
# change 就把 index_number 修改成目前的 number，以及使用 heap 把 number 出現在當前 index 給記錄下來
# find 就是先確認該 number 有沒有出現過，沒出現過一律回傳 -1 ，出現過的話就是使用 heappop 的方式，依照最小 index 的順序，逐個去確認該 index 的數值是不是 number
# 是 number 就回傳，不是的話就把 index 給 pop 掉，繼續尋找下一個 index
# 如果一直到最後都沒有找到，就代表這個 number 已經不復存在，就回傳 -1

class NumberContainers:

    def __init__(self):
        self.index_number = dict()
        self.index_list = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_number[index] = number
        heapq.heappush(self.index_list[number], index)

    def find(self, number: int) -> int:
        if number not in self.index_list:
            return -1
        while self.index_list[number]:
            idx = self.index_list[number][0]
            if self.index_number[idx] == number:
                return idx
            heapq.heappop(self.index_list[number])
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
