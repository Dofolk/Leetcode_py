# 這題是給一個樹，然後從根結點到葉子的每個路徑變成數字後，全部加起來看看是多少
# 1->2->3 = 123
# 做法就是用dfs做遍尋，然後值的部分用乘10+節點的數值來記錄，等到了葉子點的時候就可以加到全域的總和上去

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.S = 0
        self.dfs(root, 0)
        return self.S

    def dfs(self, node: Optional[TreeNode], value: int):
        if not node.left and not node.right:
            v = value*10 + node.val
            self.S += v
            return
        v = value*10 + node.val
        if node.left:
            self.dfs(node.left, v)
        if node.right:
            self.dfs(node.right, v)
