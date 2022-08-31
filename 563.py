# 這題就是來算看看一個 tree 的歪斜程度有多少，全部加起來回傳就可以了
# Tree 的歪斜與否就是看該節點的左右子樹數值總和的差距
# 所以在這題的做法就是用遞迴操作，左右子樹都給他計算一遍，然後把歪斜的數值留好相加好就可以了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def sol(root):
            if root is None:
                return 0
            L = sol(root.left)
            R = sol(root.right)
            tilt = abs(L-R)
            self.total += tilt
            return L+R+root.val
        sol(root)
        return self.total
