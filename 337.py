# 這題會給 tree，然後去搶劫，搶最多是多少
# 做法就是用 DFS 下去找，回傳包含該節點跟不包含的，想法跟之前的一樣，只是變成有兩條路走，變成兩邊都找一下就好了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))

    def dfs(self, root: Optional[TreeNode]) -> (int, int):
        if not root: return (0,0)
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return (root.val + left[1] + right[1], max(left)+max(right))
