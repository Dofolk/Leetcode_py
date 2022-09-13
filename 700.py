# 這題是要從給定的樹(BST)中找到特定的值，並回傳那個節點
# 做法就是用遞迴式找值，相同的值就回傳該節點，不同的話就依照樹值大小往左或往右去尋找

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def sol(node, v):
            if node is None:
                return None
            if node.val == v:
                return node
            if node.val < v:
                return sol(node.right,v)
            if node.val > v:
                return sol(node.left,v)
        
        cur = sol(root,val)
        
        return cur
