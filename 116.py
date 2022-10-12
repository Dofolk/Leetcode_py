# 這題是要把滿樹橫向做節點的連接
# 做法就是根據每個階層逐個操作，需要記錄幾個東西：前一個點，下一層的最左邊點以及目前的確切位置
# 當我們做完一層之後下一層就有上一層的 next 可以用，所以做比較大幅跨越的橫向移動的時候就可以用母節點做 next 移動後去定位到下一個的節點位置
# 橫向都連結完畢之後就可以往下一層邁進，直到最後

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        pre, cur, nextlv = root, root.left, root.left
        while cur:
            cur.next = pre.right
            if pre.next:
                pre.right.next = pre.next.left
                pre, cur = pre.next, pre.next.left
            else:
                pre, cur = nextlv, nextlv.left
                nextlv = nextlv.left
        return root       
