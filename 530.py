# 這題是要找 BST(binary search tree) 裡面，數值差距最小的兩個節點，他們的數值差距
# 做法就是直接跑一遍樹把值存起來，然後再找出最小的差距
# 因為是 BST，所以可以用 inorder 的順序(左->中->右)把值存好，就會是最小排到最大
# 然後有了這個這個遞增序列之後，就稍微位移一下，用 zip(v, v[1:]) 算出最小的那個

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        v = []
        
        def sol(root):
            if not root:
                return
            sol(root.left)
            v.append(root.val)
            sol(root.right)
        
        sol(root)
        
        return min(b-a for a,b in zip(v,v[1:]))
