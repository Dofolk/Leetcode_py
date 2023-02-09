# 這題是要設計 class 來做出相對應的操作
# 這題會用到一個dict來存遇到的數字跟他的位置，一個list來存遇到的數字(這邊用list是因為在getRandom比較快一點)

class RandomizedSet:

    def __init__(self):
        self.sets = dict()
        self.ls = list()

    def insert(self, val: int) -> bool:
      # 這個是要把值加進去，可以加就加並回傳True，不行就回傳False
        if val in self.sets:
            return False
        self.sets[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
      # 要做的事情跟insert差不多，只是變成remove
        if val not in self.sets:
            return False
        idx = self.sets[val]
        self.sets[self.ls[-1]] = idx
        self.ls[idx] = self.ls[-1]
        self.ls.pop()
        del self.sets[val]
        return True

    def getRandom(self) -> int:
      #取得一個隨機的數字
        return random.choice(self.ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

