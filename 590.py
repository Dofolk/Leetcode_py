# 這題是給一個 N 個分支的 Tree，然後把它做成 post-order 的 list
# 作法也是跟二元樹類似，先呼叫遞迴做好之後再將值存起來

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ls = list()
        def sol(root):
            if root is None:
                return
            for i in root.children:
                sol(i)
            self.ls.append(root.val)
        sol(root)
        return self.ls
