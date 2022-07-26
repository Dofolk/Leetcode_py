# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 基本概念就是先找到最左下角的node，接著把值存下來之後就改走每個subtree的右子樹
# 迭代法就是先定義一個要迭代的函數traversal，指令就是一直用這個函數先跑左邊，接下來把值存起來，再跑右邊
# 另一個方法就是另外開個空間stack來存走過的節點，走到底的時候存左邊的值，pop出一個最新的節點後繼續找右邊的值

# Solution 1
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        
        traversal(root)
        
        return res

# Solution 2
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while len(stack) or cur is not None:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
