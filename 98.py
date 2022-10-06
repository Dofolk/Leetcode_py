# 這題是檢查BST有沒有合法
# 做法就是遞迴處理，給定目前的最大跟最小之後開始判斷有沒有合法，然後再更新數字到左右子樹過去

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],low = -float('inf'), high = float('inf')) -> bool:
        if not root: return True
        if root.val <= low or root.val >= high: return False
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)
