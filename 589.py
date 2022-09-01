# 這題是給一個 N 分支的樹，然後要做 pre-order 的 list 出來
# 做法跟二元樹差不多，只是在做時從兩個子節點的呼叫變成 for loop 來呼叫遞迴式操作

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ls = list()
        
        def sol(root):
            if root is None:
                return
            self.ls.append(root.val)
            for i in root.children:
                sol(i)
            return
        
        sol(root)
        return self.ls
