# 這題是要做一個 dictionary，做法就是先宣告一個字典，然後再依據要求做出加值跟移除

class MyHashMap:

    def __init__(self):
        self.d = dict()

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        if key in self.d:
            return self.d[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.d:
            self.d.pop(key,None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
