# 給定一個tree，找最深的深度是多少
# 做法就是用遞迴式來做，每次操作的時候就是回傳底下節點最深的深度值，遇到最末的節點時就回傳0


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def sol(root):
            if root is None:
                return 0
            M = 0
            for i in root.children:
                M = max(M, sol(i))
            return M + 1
        
        v = sol(root)
        return v
