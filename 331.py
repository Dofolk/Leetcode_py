# 這題是給一個字串，# 代表 null，然後檢查 preorder 能不能變成一棵樹
# 做法就是算數量，遇到不是 # 的就 +1，代表說 stack(BFS) 裡面多一個節點進去，遇到 # 代表遇到 null 就要把點吐出來做另一邊

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        p = preorder.split(',')
        for n in p:
            if slot == 0:
                return False
            if n == '#':
                slot -= 1
            else:
                slot += 1
            
        return slot==0
