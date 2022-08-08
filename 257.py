# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        def paths(root,s):
            if root:
                s += str(root.val) + "->"
            if not root.right and not root.left:
                path.append(s[:-2])
            if root.right:
                paths(root.right,s)
            if root.left:
                paths(root.left,s)
        paths(root,"")
        return path
      
# 這題要輸出在樹裡面的每個路徑
# 用遞回來找出每個路徑
# 如果不是 NULL 就存植跟加箭頭
