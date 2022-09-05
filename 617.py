# 這題是要把兩個樹作合併，值劫整個蝶合作相加，所以其中一個有樹枝的話結果的同樣地方就一定會有樹枝
# 做法就是用遞迴式來做，把 tree 1 當成修改的目標，修改每個節點的連結點
# 其中一個節點如果是空的話就回傳另一個節點，最後就是把 tree 1 的點加值，再把 tree 1 的連結子點做修改就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def sol(r1,r2):
            if r1 is None:
                return r2
            if r2 is None:
                return r1
            r1.val += r2.val
            r1.left = sol(r1.left,r2.left)
            r1.right = sol(r1.right,r2.right)
            return r1
        
        root1 = sol(root1,root2)
        return root1
