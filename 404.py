# 這題要把所有左葉子的值加起來
# 第一個方法就是用 recursive 做，先判斷最一開始的 root 是不是空的，然後往下找不是左子葉就回傳0，是就加 node 的值
# 第二個方法就是用 iterative 做，判斷左邊節點是不是葉子。是的話就可以加起來，不是的話就存到 stack 去等下一輪操作


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
# Solution 1
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def sol(root, is_left):
            if root.left is None and root.right is None:
                return root.val if is_left else 0
            
            v = 0
            if root.left:
                v += sol(root.left, True)
            if root.right:
                v += sol(root.right, False)
            
            return v
        
        return sol(root,False)
      
# Solution 2
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        stack = [root]
        def is_leaf(root):
            return root.left is None and root.right is None and root is not None
        while stack:
            cur = stack.pop()
            if is_leaf(cur.left):
                s += cur.left.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
          
        return s
