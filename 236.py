# 這題是給一個tree，然後找兩個點的最近祖先是誰
# 做法就先用一個 dict() 來存每個點的父輩是誰，直到兩個目標點都在 dict() 裡面
# 然後做一個 set 逐序存其中一個點的往上路徑，然後用另一個點去找看看路徑裡面那個點先遇到

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
