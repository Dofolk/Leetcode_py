# 這題是給一個 BST ，然後要找第k小的值是多少
# 直接做 inorder，然後回傳第 k-1 個就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k-1]
