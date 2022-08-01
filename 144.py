# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
# Solution 1  
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        stack = []
        
        cur = root
        
        while stack or cur is not None:
            while cur:
                stack.append(cur)
                ls.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
    
        return ls
    
# Solution 2
