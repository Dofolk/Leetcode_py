# 這題是要把 tree 做成字串，然後要加上 ()
# 自己如果是空的就回傳空的值，沒有子代的話直接回傳自己的數值，如果右子代為空就回傳自己的數字+(左子代的內容)，剩下的就回傳最長的回復
# 這題算起來....不太好懂，真的不好懂，可以的話就嘗試原文理解吧

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def sol(root):
            if root is None:
                return str()
            if root.left is None and root.right is None:
                return str(root.val)
            if root.right is None:
                return str(root.val)+"("+sol(root.left)+")"
            return str(root.val) + "(" + sol(root.left) + ")(" + sol(root.right) + ")"
        
        return sol(root)
