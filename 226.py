# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def verse(root):
            if root is None:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            verse(root.left)
            verse(root.right)
        
        verse(root)
        
        return root
      
# 這題要把 tree 以根結點做鏡射
# 用遞迴來做，反正鏡射的話每個節點都要做左右調換，所以遞迴一個一個交換就可以了
