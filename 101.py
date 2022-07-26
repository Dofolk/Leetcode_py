# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def sol(l_root,r_root):
            if l_root is None or r_root is None:
                return (l_root == r_root)
            if l_root.val != r_root.val:
                return False
            return sol(l_root.left,r_root.right) and sol(l_root.right,r_root.left)
        return sol(root.left,root.right)
      
# 用遞回做，一次就是比對對應位置的值有沒有一樣
