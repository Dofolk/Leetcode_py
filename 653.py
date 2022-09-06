# 這題是要找 tree 裡面有沒有兩個節點相加的值剛好是想要的值
# 做法是用遞回來做，走過之後就把差值丟進一個 set()，遇到有在 set() 裡面的數字時就可以回傳了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = {}
        def sol(root):
            if root is None:
                return False
            if root.val in values:
                return True
            values[k-root.val] = True
            return sol(root.left) or sol(root.right)
        
        return sol(root)
