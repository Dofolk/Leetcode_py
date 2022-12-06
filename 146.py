# 這題是要做 LRU 的操作，關於LRU可以看 "參考資料"
# 這邊是用 orderedDict 來操作，最近使用的就放在整個序列字典的最後面
# 所以當要移除不常用的東西或重新使用數值時，就先移除原本的東西後再重新新增一次就可以啦

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain >0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
