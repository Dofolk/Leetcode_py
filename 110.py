# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root: TreeNode) -> (bool,int):
        if not root:
            return (True, 0)
        
        left_balance, left_height = self.solve(root.left)
        if not left_balance:
            return (False, 0)
        
        right_balance, right_height = self.solve(root.right)
        if not right_balance:
            return (False, 0)
        return ( abs(left_height - right_height) < 2, max(left_height, right_height) + 1 )
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.solve(root)[0]
      
# 用遞回來做，要記錄之前判斷的結果跟高度，下一次處理的時候才可以避免出錯
