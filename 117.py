# 這題是要做把樹的節點都左右相連結在一起，但是~有可能有些地方是沒有點的
# 做法是用 3 個 pointer 來處理，一個紀錄父點，一個紀錄最左邊點，一個就往下跑做左右連結
# 這邊就是用 cur 先去找最左邊的點，然後做出連結，同時因為 cur = Lv ，所以找到點之後 Lv就會卡在最左邊點，因為後面都是 cur 在跑在運作都沒有去動 Lv，藉以固定最左邊點
# 後面等到一層都跑完之後，就把 cur 拉回去變成 0 點，然後把 Lv 抓住的最左邊點變成下一個要開頭的父點！

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        pre = root
        cur = Lv = Node(0)
        
        while pre:
            cur.next = pre.left
            if cur.next:
                cur = cur.next
            cur.next = pre.right
            if cur.next:
                cur = cur.next
            pre = pre.next
            if not pre:
                cur = Lv
                pre = Lv.next
        return root
