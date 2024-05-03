# 這題是給樹然後找每一列最大的值是多少
# 作法就是有個東西存第幾層的最大數字是多少，然後在回傳就好
# 使用 dfs 的時候就去確認數字有沒有比較大(用defaultdict+整理list)及層數有沒有存在(單一list)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1 defaultdict+list
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        D = collections.defaultdict(lambda: -float('inf'))
        
        def dfs(node, depth):
            if not node:
                return
            if D[depth] < node.val:
                D[depth] = node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return
        dfs(root, 0)
        res = []
        for i in range(max(D.keys()) + 1):
            res.append(D[i])
        return res

# Solution 2 single list
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            res[depth] = max(node.val, res[depth])
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res
