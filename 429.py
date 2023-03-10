# 這題是要做 n node tree 的 level order traversal
# 做法是 BFS，用一個 deque 來存要做的點，把一層的所有東西都先加進去，然後再逐個處理

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        
        if not root:
            return res
        
        q = deque([root])
        
        while q:
            lv = []
            for _ in range(len(q)):
                node = q.popleft()
                lv += [node.val]
                for n in node.children:
                    q.append(n)
            res += [lv]
        return res
