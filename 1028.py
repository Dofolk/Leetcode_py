# 這題是要把 preorder 的結果把 tree 給恢復回來
# 這部分可以用 DFS 重新給建回來

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        next_level, next_node, pos = 0, 0, 0
        while pos < len(traversal) and traversal[pos].isdigit():
            pos += 1
        root = TreeNode(int(traversal[:pos]))
        def dfs(node, level):
            nonlocal next_level, next_node, pos
            if pos < len(traversal)-1:
                next_level, next_node, pos = self.next_step(pos, traversal)
            else:
                next_level, next_node = -1, -1
            if level == next_level:
                node.left = TreeNode(next_node)
                dfs(node.left, level + 1)
            if level == next_level:
                node.right = TreeNode(next_node)
                dfs(node.right, level + 1)
            return
        
        dfs(root, 1)

        return root
    def next_step(self, pos, traversal):
        next_level = 0
        digit_count = 0
        while not traversal[pos].isdigit():
            next_level += 1
            pos += 1
        while pos < len(traversal) and traversal[pos].isdigit():
            digit_count += 1
            pos += 1
        return next_level, int(traversal[pos - digit_count:pos]), pos
