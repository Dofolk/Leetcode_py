# 這題是要把一個樹變成只有右邊一條的 preordered link list(意思就是左節點是None)
# 做法就是 preorder 走一遍之後再逐個點做重新連結
# 還有個做法就是把每個點的右子樹都拉到該節點的最右下角，然後再移動左子樹到右邊去，最後把左邊掛上 None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        ls = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                ls.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        for i in range(len(ls)):
            if i == len(ls)-1:
                ls[i].left = None
                ls[i].right = None
            else:
                ls[i].left = None
                ls[i].right = ls[i+1]
                
                
                
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
