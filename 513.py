# 這題是要找樹的最左下的點
# 這題有很多種做法，這裡主要講 DFS 跟 Queue
# DFS的做法就是一直往下往左去找，以深度為主然後再去找左邊的點，一直迭代到底就好了，最後再依據深度決定數字
# 
# Queue的方法就是把點依照先右後左放進Queue裡面，然後一個一個拉出來記錄數值跟存放更深的節點的，這樣可以跑遍所有的點
# 同時也因為是從右往左放，所以可以保證最後那個節點是最底層也是最左邊的點


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
class Solution:
    val = float('inf')
    dep = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return
            left, right = dfs(node.left, depth + 1), dfs(node.right, depth + 1)
            if node and depth > self.dep and not (node.right or node.left):
                self.val = node.val
                self.dep = depth
            return node
        dfs(root, self.dep)

        return self.val if self.dep > 0 else root.val

# Solution 2
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmost_val = None

        while queue:
            node = queue.popleft()
            
            leftmost_val = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return leftmost_val
