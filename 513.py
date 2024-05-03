# 這題是要找最左下的點


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = float('inf')
    dep = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return
            left, right = dfs(node.left, depth + 1), dfs(node.right, depth + 1)
            if node and depth > self.dep and not (node.right or node.left):
                self.val = node.val
                self.dep = depth
            return node
        dfs(root, self.dep)

        return self.val if self.dep > 0 else root.val
