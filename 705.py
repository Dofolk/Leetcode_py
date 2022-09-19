# 這題是要設計一個函數，宣告出一個 set 然後做加入、移除跟檢查有沒有在內
# 用 python 原有的那些函數就可以完成了，在 remove 的部分用 discard 來確保移除目標不在set內的狀況會回傳error

class MyHashSet:

    def __init__(self):
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
