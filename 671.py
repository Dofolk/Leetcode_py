# 這題是要找出所有節點值第二小的是多少
# 做法就是先令 0 跟 INF，然後逐個點去走並記錄目前第二大的是多少
# 因為題目特行，讓最一開始的 root 值會是最小的，所以就是望下去找
# 還有一種做法就是暴力解，直接走一遍存所有值找第二大的

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        m = root.val
        
        def sol(root):
            if root:
                if m < root.val < self.ans:
                    self.ans = root.val
                elif root.val == m:
                    sol(root.left)
                    sol(root.right)
        
        sol(root)
        return self.ans if self.ans<float('inf') else -1
