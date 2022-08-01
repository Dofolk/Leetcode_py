# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        
        def travel(root):
            if root is None:
                return
            travel(root.left)
            travel(root.right)
            ls.append(root.val)
        
        travel(root)
        
        return ls
      
# 把tree做成 postorder，用recursive來做
