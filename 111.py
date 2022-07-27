# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not any([root.left,root.right]):
            return 1
        
        min_depth = float('inf')
        for c in [root.left,root.right]:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1
     
# 遞回來做
# 要設置每次從結點往下找的時候，下面兩個子節點有沒有存在，不存在直接回覆1(原始節點的高度1)
# 要確認好兩個子節點都要不存在，這樣才算是一條有意義的path，才能算長度
